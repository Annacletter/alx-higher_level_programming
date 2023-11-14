#!/usr/bin/node

// Returns the number of args already printed
// and the new arg value
const stack = [];
exports.logMe = function (item) {
  stack.push(item);
  console.log(stack.indexOf(item) + ': ' + item);
};
