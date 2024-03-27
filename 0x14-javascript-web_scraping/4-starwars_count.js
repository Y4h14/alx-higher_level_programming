#!/usr/bin/node
const args = process.argv;
const req = require('request');
req(args[2].replace('films', 'people') + '/18',
  function (err, res, body) {
    if (err) {
      console.error(err);
    }
    const result = JSON.parse(body);
    console.log(result.films.length);
  });
