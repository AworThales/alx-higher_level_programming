#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const { argv } = require('process');
const num4 = parseInt(argv[2]);
const num5 = parseInt(argv[3]);
console.log(add(num4, num5));
