#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
let textA = '';
let textB = '';
fs.readFile(fileA, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    textA = data;
    processFiles();
  }
});
fs.readFile(fileB, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    textB = data;
    processFiles();
  }
});
function processFiles () {
  if (textA && textB) {
    fs.writeFile(fileC, textA + textB, 'utf8', function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
}
