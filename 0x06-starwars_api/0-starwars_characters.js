#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Provide movie id');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('error: ', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`Failed to retrive data. Status code ${response.statuscode}`);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('error: ', error);
        return;
      }
      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
});
