#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  
  print() {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while(y < this.width) {
        myVar += 'X';
	y++;
      }
      console.log(myVar);
    }
  }

  rotate() {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    width *= 2;
    height *= 2;
  }
<<<<<<< HEAD
=======
 }
>>>>>>> ed99eae42a61b1d7f76e82e7570c7fc0efea0252
  module.exports = Rectangle;
