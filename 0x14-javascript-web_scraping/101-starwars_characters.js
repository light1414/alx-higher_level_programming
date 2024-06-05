#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

function getCharacterTitleInOrder (movieId) {
  const apUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
  request.get({ url: apUrl, json: true }, function (error, respo, body) {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const characters = body.characters;
      const promises = characters.map((url) => {
        return new Promise((resolve, reject) => {
          request.get({ url, json: true }, function (error, respo, body) {
            if (error) {
              reject(error);
            } else {
              resolve(body.name);
            }
          });
        });
      });

      Promise.all(promises)
        .then((names) => console.log(names.join('\n')))
        .catch((error) => console.error(error));
    } else {
      console.error(`Request failed with status code ${response.statusCode}`);
    }
  });
}

if (args[0]) {
  const movieId = args[0];
  getCharacterTitleInOrder(movieId);
}
