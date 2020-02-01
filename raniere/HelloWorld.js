const args = process.argv;
let   name = "World";

if (args && (args.length > 2)) name = args[2];

console.log(`Hello, ${name}!`);