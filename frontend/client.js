import net from "net";
import data from "./sendData.js";

const address = "/tmp/server_socket_1101";
const client = net.createConnection(address);

const encodeUTF8 = (str) => {
  const encoder = new TextEncoder();
  return encoder.encode(str);
};

const decodeUTF8 = (buffer) => {
  const decoder = new TextDecoder();
  return decoder.decode(buffer);
};

client.on("connect", () => {
  console.log("サーバに接続しました。");
  console.log("次のデータを送信。", data);
  client.write(JSON.stringify(data));
});

// serverから送信されたデータを表示。
client.on("data", (data) => {
  console.log("次のデータを受信しました。", decodeUTF8(data));
  client.end();
});

client.on("error", (error) => {
  console.log("エラーが発生しました。");
  console.log(error.message);
});

client.on("end", () => {
  console.log("切断しました。");
  client.destroy();
});

client.on("close", () => {
  console.log("Connection is closed");
});
