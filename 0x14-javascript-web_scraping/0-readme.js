#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (err, info) {
  if (info) {
    console.log(info);
  } else {
    console.log(err);
  }
});
