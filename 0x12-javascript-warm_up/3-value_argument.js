#!/usr/bin/node
const { argv } = require('process');
let t = 0;
argv.forEach(() => t++);
console.log(t === 2 ? 'No argument' : argv[2]);
