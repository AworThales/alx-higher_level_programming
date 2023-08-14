#!/usr/bin/node

const { argv } = require('process');
const arg = argv.slice(2);
let ans = 0;
let finishArray = [];

if (arg.length > 1) {
  finishArray = [...new Set(arg.map((e) => parseInt(e)).sort((a, b) => b - a))];
  ans = finishArray.length > 1 ? finishArray[1] : finishArray[0];
}
console.log(ans);
