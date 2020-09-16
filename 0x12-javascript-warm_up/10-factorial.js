#!/usr/bin/node

function recursiveFactorial (n) {
  if (n <= 1) {
    return n;
  }

  return n * recursiveFactorial(n - 1);
}

const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
  console.log('1');
} else {
  console.log(recursiveFactorial(num));
}
