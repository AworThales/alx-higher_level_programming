#!/usr/bin/node

const { argv } = require('process');
function factorial (numba) {
  if (numba <= 1) return (1);
  return (factorial(numba - 1) * numba);
}
const parsed = parseInt(argv[2]);
console.log(Number.isNaN(parsed) ? 1 : factorial(parsed));
