const fake = require("warden-demo-fake-pkg-93817");
const api_key = "abcd1234efgh5678ijkl9012mnop3456";

function run(userInput) {
  return eval(userInput);
}

const make = new Function("a", "b", "return a + b");
module.exports = { fake, api_key, run, make };
