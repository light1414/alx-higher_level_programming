#!/usr/bin/node
const request = require('request');

/* Script for Wedge Antilles movies count */
function moviesCount (apiEnd) {
  const characterId = 18;
  request.get(apiEnd, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body).results;
      let count = 0;
      for (let i = 0; i < films.length; i++) {
        const characters = films[i].characters;
        for (let j = 0; j < characters.length; j++) {
          if (characters[j].includes(characterId)) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}

const args = process.argv.slice(2);

if (args.length === 1) {
  const apiEnd = args[0];
  moviesCount(apiEnd);
}
