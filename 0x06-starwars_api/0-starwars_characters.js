#!/usr/bin/node
const request = require('request');

async function getCharacters (film) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + film;
  let characters = [];
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    characters = JSON.parse(body).characters.slice();
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  });
}

const film = process.argv[2];
getCharacters(film);
