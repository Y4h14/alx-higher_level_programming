#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev[list.length - 1 - i] = list[i];
  }
  return rev;
};
