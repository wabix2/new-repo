// Warden CI test file. Everything here is fake.
const fake = require("warden-demo-fake-pkg-93817");   // nonexistent package
const apiKey = "AKIAIOSFODNN7EXAMPLE";                // fake AWS-style example key
const password = "SuperSecretPassw0rd123!";           // fake hardcoded password

function run(userInput) {
  return eval(userInput);                              // dangerous dynamic execution
}

const make = new Function("a", "b", "return a + b");   // dangerous dynamic execution

module.exports = { fake, apiKey, password, run, make };
