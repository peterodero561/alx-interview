#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  const characterNames = new Array(characters.length); // Array to hold character names in order

  let completedRequests = 0;

  // Loop through each character URL and make requests
  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        characterNames[index] = characterData.name; // Store the name in the correct order
        completedRequests += 1;

        // Only print once all requests have completed
        if (completedRequests === characters.length) {
          characterNames.forEach((name) => console.log(name));
        }
      }
    });
  });
});
