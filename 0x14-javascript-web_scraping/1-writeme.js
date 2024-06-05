#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, data) {
  fs.writeFile(filePath, data, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
}

const args = process.argv.slice(2);

if (args.length < 1) {
  console.log('No args passed');
} else {
  const filePath = args[0];
  const data = args[1];
  writeToFile(filePath, data);
}
