#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const element in list) {
    if (list[element] === searchElement) {
      counter++;
    }
  }
  return counter;
};
