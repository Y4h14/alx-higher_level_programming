#!/usr/bin/node
const args = process.argv;
let i = 2;
let max = parseInt(args[2]);
let semiMax = 0;
while (args[i] !== undefined) {
  if (args[i] > max) {
    semiMax = max;
    max = parseInt(args[i]);
  } else if (args[i] > semiMax) {
    semiMax = parseInt(args[i]);
  }
  i++;
}
if (args[3] === undefined) {
  semiMax = 0;
}
console.log(semiMax);
