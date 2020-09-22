#!/usr/bin/node

const arr = require('./100-data.js').list;
let i = 0;
const map1 = arr.map(n => n * i++);
console.log(arr);
console.log(map1);
