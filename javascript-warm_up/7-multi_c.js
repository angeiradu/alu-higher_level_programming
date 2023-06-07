#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrence');
} else {
  const x = parseInt(arg);
  let count = 0;
  while(count < x) {
    console.log('C is fun');
    count++;
  }
}
