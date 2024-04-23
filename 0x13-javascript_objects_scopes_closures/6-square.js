#!/usr/bin/node

const OddSquare = require('./5-square');
class Square extends OddSquare {
  charPrint (c) {
    if (c === null) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
