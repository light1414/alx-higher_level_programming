#!/usr/bin/node

/*lets code*/
const fs = require('fs');

const contentA = process.argv[2];
const contentB = process.argv[3];
const contentC = process.argv[4];

const fileA = fs.readFileSync(contentA, 'utf8');
const fileB = fs.readFileSync(contentB, 'utf8');
const fileC = dataA + dataB;

fs.writeFileSync(contentC, contentC);
