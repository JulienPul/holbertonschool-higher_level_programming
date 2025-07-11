#!/usr/bin/node

const args_Count = process.argv - 2;

if (args_Count === 0) {
  console.log('No argument');
} else if (args_Count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
