#!/usr/bin/node
const { dict } = require('./101-data');
let values = [];
const result = {};
for (const key in dict) {
  values.push(dict[key]);
}
values = [...new Set(values)];

for (const item of values) {
  result[item] = [];
  for (const key in dict) {
    if (item === dict[key]) {
      result[item].push(key);
    }
  }
}
console.log(result);
