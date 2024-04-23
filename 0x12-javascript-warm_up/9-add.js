#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const arg0 = process.argv[2];
const arg1 = process.argv[3];

console.log(add(arg0, arg1));
