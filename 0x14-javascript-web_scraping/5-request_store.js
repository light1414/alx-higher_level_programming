#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);

function scrapeWebPageToFile (url, fileTitle) {
  request.get(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      fs.writeFile(fileTitle, body, 'utf8', function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}

if (args.length === 2) {
  const url = args[0];
  const fileTitle = args[1];
  scrapeWebPageToFile(url, fileTitle);
}
