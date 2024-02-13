#!/usr/bin/node
exports.converter = function (base) {
  const setBase = base;
  return function (num) {
    return num.toString(setBase);
  };
};
