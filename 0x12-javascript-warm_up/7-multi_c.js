#!/usr/bin/node

const { argv } = require('process');
const numba = parseInt(argv[2]);
const printC = (cuantity) => {
  for (; cuantity > 0; cuantity--) console.log('C is fun');
};
Number.isInteger(numba) ? printC(numba) : console.log('Missing number of occurrences');
