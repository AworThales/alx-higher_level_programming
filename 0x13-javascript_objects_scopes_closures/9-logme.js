#!/usr/bin/node
let qty = 0;
const logMe = (item) => {
  console.log(`${qty}: ${item}`);
  qty++;
};
module.exports = { logMe };
