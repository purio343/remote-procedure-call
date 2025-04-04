import readline from "readline";
import { v4 as uuidv4 } from "uuid";

const encodeUTF8 = (string) => {
  return new TextEncoder().encode(string);
};

const decodeUTF8 = (buffer) => {
  return new TextDecoder().decode(buffer);
};

const input = async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise((resolve) => {
    rl.question("> ", (answer) => {
      rl.close();
      resolve(answer.trim());
    });
  });
};

const generateUUID = () => {
  return uuidv4();
};

export { encodeUTF8, decodeUTF8, input, generateUUID };
