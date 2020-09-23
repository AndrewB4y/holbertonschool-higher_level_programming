#!/usr/bin/node

const request = require('request');

const args = process.argv;
let count = 0;

request(
  {
    method: 'GET',
    uri: args[2]
  }, function (error, response, body) {
    if (error) throw error;
    JSON.parse(body).results.forEach(function (film) {
      film.characters.forEach(function (chtr) {
        if (chtr.includes('18')) count++;
      });
    });
    console.log(count);
  }
);
