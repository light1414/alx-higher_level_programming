#!/usr/bin/node

const numb = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const sortedNumb = numb.sort((a, b) => b - a);
  console.log(sortedNumb[1]);
}
