#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  const num = parseInt(arg);
  for (let i = 0; i < num; i++) {
    console.log('X');
  } for (let j = 0; j > i; j++) {
    console.log('X');
  }
}
