#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

function completedUserTask (Url) {
  request.get(Url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const json = JSON.parse(body);
      const completed = {};
      for (const task of json) {
        if (task.completed === true) {
          /* new key with no value */
          if (completed[task.userId] === undefined) {
            completed[task.userId] = 1;
            /* if the key exists increment the value of the key */
          } else {
            completed[task.userId]++;
          }
        }
      }
      console.log(completed);
    }
  });
}

if (args.length === 1) {
  const Url = args[0];
  completedUserTask(Url);
}
