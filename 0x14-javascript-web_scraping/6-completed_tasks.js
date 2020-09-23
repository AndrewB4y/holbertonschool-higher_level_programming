#!/usr/bin/node

const request = require('request');

const args = process.argv;
const url = args[2];
const out = {};

function count (todo) {
  if (todo.completed) {
    if (typeof out[todo.userId.toString()] === 'undefined') {
      out[todo.userId.toString()] = 1;
      return;
    }
    out[todo.userId.toString()] = out[todo.userId.toString()] + 1;
  }
}

request(
  {
    method: 'GET',
    uri: url
  },
  function (error, response, body) {
    if (error) throw error;
    if (response.statusCode === 200) {
      JSON.parse(body).forEach(count);
      console.log(out);
    }
  }
);
