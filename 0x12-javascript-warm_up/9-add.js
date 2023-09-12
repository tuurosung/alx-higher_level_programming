#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
function add (a, b) {
    return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
