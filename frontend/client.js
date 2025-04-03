import net from "net";
import { encodeUTF8, decodeUTF8, input } from "./utils.js";
import { readFile } from "fs/promises";

// Todo: クラスベースの処理に改善。

const config = JSON.parse(await readFile("./frontend/config.json"));
const method = await input();
let data;
try {
  data = JSON.parse(await readFile(`./frontend/sampleData/${method}.json`));
} catch (e) {
  console.error(
    `指定されたファイルが見つかりません。\n既存のファイルを選択してください。\nファイル：${method}.json`
  );
  process.exit(1);
}
const address = config["address"];
const client = net.createConnection(address);

let buffer = "";

client.on("connect", () => {
  console.log("サーバに接続。");
  console.log("次のデータを送信。", data);
  client.write(encodeUTF8(JSON.stringify(data)));
});

// serverから送信されたデータを表示。
client.on("data", (chunk) => {
  buffer += decodeUTF8(chunk);
  // JSONオブジェクトに変換
  const response = JSON.parse(buffer);
  console.log("次のデータを受信。", response);
  buffer = "";
  client.end();
});

client.on("error", (error) => {
  console.log("エラーが発生。");
  console.log(error.message);
  client.destroy();
});

client.on("end", () => {
  console.log("切断しました。");
});

client.setTimeout(config["timeout"]);

client.on("timeout", () => {
  console.error("接続がタイムアウト。");
  client.destroy();
});
