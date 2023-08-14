#!/usr/bin/node
const { argv } = require('process');
const numba = parseInt(argv[2]);
console.log(Number.isInteger(numba) ? `My number: ${numba}` : 'Not a number');
