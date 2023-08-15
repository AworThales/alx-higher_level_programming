#!/usr/bin/node
const fs = require('fs');
const tArg = fs.readFileSync(process.argv[2]).toString();
const awArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], tArg + awArg);
