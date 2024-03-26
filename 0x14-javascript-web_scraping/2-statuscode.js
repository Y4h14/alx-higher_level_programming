#!/usr/bin/node
const args = process.argv;
const req = require('request');

req(args[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  console.log('code:', res.statusCode);
});
