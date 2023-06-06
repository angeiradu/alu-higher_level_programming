#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg === 0) {
  console.log('No argument');
} else if (arg === 1) {
  console.log('HBTN');
} else {
  console.log('HBTN cool');
}  
  
