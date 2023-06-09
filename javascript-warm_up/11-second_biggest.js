#!/usr/bin/node

function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) { return (0); }

  let biggest = myArray[2];
  let secondbiggest = myArray[3];

  for (let i = 2; i < myArray.length; i++) {
    if (myArray[i] > biggest) {
      secondbiggest = biggest;
      biggest = myArray[i];
    } else if (myArray[i] > secondbiggest && myArray[i] < biggest) {
      secondbiggest = myArray[i];
    }
  }
  return (secondbiggest);
}

console.log(second(process.argv));	
