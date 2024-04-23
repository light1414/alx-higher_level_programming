#!/usr/bin/node
const sizeOfSquare = parseInt(process.argv[2]);

if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeOfSquare; i++) {
    console.log('X'.repeat(sizeOfSquare));
  }
}
