#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

function getCharacterTitle (movieId) {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
  request.get(apUrl, function (error, respo, body) {
    if (error) {
      console.log(error);
    } else {
      const json = JSON.parse(body);
      for (const character of json.characters) {
        request.get(character, function (error, respo, body) {
          if (error) {
            console.log(error);
          } else {
            const json = JSON.parse(body);
            console.log(json.name);
          }
        });
      }
    }
  });
}

if (args.length === 1) {
  const movieId = args[0];
  getCharacterTitle(movieId);
}
