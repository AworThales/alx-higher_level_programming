#!/usr/bin/node
const { argv } = require('process');
const my_number = parseInt(argv[2]);
console.log(Number.isInteger(my_number) ? `My number: ${my_number}` : 'Not a number');
