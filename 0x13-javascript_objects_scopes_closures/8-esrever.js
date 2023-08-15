#!/usr/bin/node
const esrever = (list) => {
  const arrayReverse = [];
  list.forEach((element) => arrayReverse.unshift(element));
  return (arrayReverse);
};

module.exports = { esrever };
