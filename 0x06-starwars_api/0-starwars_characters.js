#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;
request(url, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const acharacters = JSON.parse(body).characters;
    for (const character in acharacters) {
      const ress = await new Promise((resolve, reject) => {
        request(acharacters[character], (err, ress, html) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(ress);
    }
  }
});
