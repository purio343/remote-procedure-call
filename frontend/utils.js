const encodeUTF8 = (string) => {
  return new TextEncoder().encode(string);
};

const decodeUTF8 = (buffer) => {
  return new TextDecoder().decode(buffer);
};

export { encodeUTF8, decodeUTF8 };
