#!/usr/bin/node

const aDict = require('./101-data.js').dict;

const myDict = {};

for (const key in aDict) {
  if (typeof myDict[aDict[key]] === 'undefined') {
    myDict[aDict[key]] = [key];
    continue;
  }
  myDict[aDict[key]].push(key);
}
console.log(myDict);
