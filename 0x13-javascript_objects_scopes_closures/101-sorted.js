#!/usr/bin/node
const {dict} = require('./101-data');
let values = [];
const result = {};
for (let key in dict) {
  values.push(dict[key]);
}
values = [... new Set(values)];

for (let item of values) {
  result[item] = [];
  for (let key in dict) {
    if (item === dict[key]) {
      result[item].push(key); 
    }
  }
}
console.log(result);
