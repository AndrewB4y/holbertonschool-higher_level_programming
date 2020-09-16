#!/usr/bin/node

let argc = 0;
const args = process.argv;
args.forEach((val, index) => {
  argc = argc + 1;
});

if (argc < 3) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
