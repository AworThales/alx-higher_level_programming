#!/usr/bin/node

const { argv } = require('process');
const sizes = parseInt(argv[2]);
const printSquare = (sizes) => {
  const ros = 'X'.repeat(sizes);
  for (let t = 0; t < sizes; t++) console.log(ros);
};
Number.isInteger(sizes) ? printSquare(sizes) : console.log('Missing sizes');
