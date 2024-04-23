#!/usr/bin/node

const list = require('./100-data').list;
const firstList = list.map((value, index) => value * index);
console.log(list);
console.log(firstList);
