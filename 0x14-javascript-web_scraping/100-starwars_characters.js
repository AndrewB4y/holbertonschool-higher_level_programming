#!/usr/bin/node

const request = require('request');

const args = process.argv;
const fid = args[2];

request(
  {
    method: 'GET',
    uri: 'https://swapi-api.hbtn.io/api/films/' + fid
  },
  reqFilm
);

function reqFilm (error, response, body) {
  if (!error && response.statusCode === 200) {
    JSON.parse(body).characters.forEach(printChtr);
  }
}

function printChtr (item, index) {
  request(
    {
      method: 'GET',
      uri: item
    },
    function (error, response, body) {
      if (!error && response.statusCode === 200) {
        console.log(JSON.parse(body).name);
      }
    }
  );
}
