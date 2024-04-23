#!/usr/bin/node

/* lets code*/
let counter = 0;

exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
