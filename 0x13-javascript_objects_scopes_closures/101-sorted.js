#!/usr/bin/node
const { dict } = require('./101-data');
const convertedArr = Object.entries(dict);
const freshObj = {};
convertedArr.forEach(item => {
  freshObj[item[1]] ? freshObj[item[1]].push(item[0]) : freshObj[item[1]] = [item[0]];
});

console.log(freshObj);
