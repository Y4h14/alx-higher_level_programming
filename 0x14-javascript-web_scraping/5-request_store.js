#!/usr/bin/node
const args = process.argv;
const req = require('request');
const fs = require('node:fs');

req(args[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const result = body;
  fs.writeFile(args[3], result, err => {
    if (err) {
      console.error(err);
    }
  });
});
