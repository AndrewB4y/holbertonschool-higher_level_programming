#!/usr/bin/node

exports.addMeMaybe = function (n, f) {
  n = n + 1;
  f(n);
};
