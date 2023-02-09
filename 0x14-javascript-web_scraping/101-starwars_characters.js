#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

/* Make the request to the film */
request.get(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const data = JSON.parse(body);
  /* Call display with the character's arrays */
  display(data.characters, 0);
});

/* request to the each character and display */
function display (person, index) {
  if (!person[index]) {
    return;
  }
  request.get(person[index], (error, response, body) => {
    if (error) {
      console.error('error:', error);
    }
    const OneCharacter = JSON.parse(body);
    console.log(OneCharacter.name);
    display(person, ++index);
  });
  return 0;
}
