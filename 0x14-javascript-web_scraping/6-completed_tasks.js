#!/usr/bin/node
const args = process.argv;
const req = require('request');

req(args[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const completed = {};
  const result = JSON.parse(body);
  for (const i in result) {
    const task = result[i];
    if (task.completed === true) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  }
  console.log(completed);
});
