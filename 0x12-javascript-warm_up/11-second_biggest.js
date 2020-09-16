#!/usr/bin/node

const nums = process.argv;

if (nums.length < 4) {
  console.log(0);
} else {
  let arr = nums.slice(2, nums.length);
  arr = arr.map(n => parseInt(n));
  arr = arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
