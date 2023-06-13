#!/usr/bin/node
const filename = process.argv[2];
const content = process.argv[3];
fs.writeFile(filiname, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
