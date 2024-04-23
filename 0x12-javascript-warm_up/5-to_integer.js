#!/usr/bin/node

const numOne = parseInt(process.argv[2]);

if (isNaN(numOne)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numOne}`);
}  
