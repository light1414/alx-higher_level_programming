#!/usr/bin/node

const argOne = process.argv[2];

if (argOne) {
  console.log(argOne);
} else {
  console.log('No argument');
}
