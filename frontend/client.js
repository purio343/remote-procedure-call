import net from "net";
import data from "./sendData.js";
import { encodeUTF8, decodeUTF8 } from "./utils.js";

const address = "/tmp/server_socket_1101";
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

client.setTimeout(5000);

client.on("timeout", () => {
  console.error("接続がタイムアウト。");
  client.destroy();
});
