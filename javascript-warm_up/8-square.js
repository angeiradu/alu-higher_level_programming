#!/usr/bin/node
const num = process.argv[2];

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let a = '';
    for (let j = 0; j < num; j++) {
      a = a + 'X';
    }
    console.log(a);
  }
}
