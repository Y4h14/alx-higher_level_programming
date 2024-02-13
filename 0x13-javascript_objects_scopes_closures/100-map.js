#!/usr/bin/node
const { list } = require('./100-data.js');
const resultList = list.map((x, index) => x * index);
console.log(list);
console.log(resultList);
