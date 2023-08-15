#!/usr/bin/node
const nbOccurences = (list, searchElement) => list.filter((item) => searchElement === item).length;
module.exports = { nbOccurences };
