#!/usr/bin/node
exports.converter = function (base) {
  return function (numba) {
    return numba.toString(base);
  };
};
