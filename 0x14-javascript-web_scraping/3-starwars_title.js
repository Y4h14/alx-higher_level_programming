#!/usr/bin/node
const args = process.argv;
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

req(url + args[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const result = JSON.parse(body);
  console.log(result.title);
});
