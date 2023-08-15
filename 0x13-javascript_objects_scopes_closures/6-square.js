#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let t = 0; t < this.height; t++) {
      let s = '';
      for (let y = 0; y < this.width; y++) {
        s += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
