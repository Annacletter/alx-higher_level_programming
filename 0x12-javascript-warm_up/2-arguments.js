#!/usr/bin/node

const argCount = process.argv.length;

if (argCount < 3) {
  console.log('No arguments');
} else if (argCount === 3) {
  console.log('One argument found');
} else {
  console.log('Multiple arguments found');
}
