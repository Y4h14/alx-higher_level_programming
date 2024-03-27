#!/usr/bin/node
const args = process.argv;
const req = require('request');
req(args[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const results = JSON.parse(body).results;
  const result = results.reduce((count, movie) => {
    return movie.characters.find((character) =>
      character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0);
  console.log(result);
});
