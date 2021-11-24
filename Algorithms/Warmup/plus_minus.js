// Language: JavaScript (Node.js)

let p = 0;
let n = 0;
let z = 0;

for (let i = 0; i < arr.length; i++) {
  if (arr[i] > 0) {
    p += 1;
  } else if (arr[i] == 0) {
    z += 1;
  } else {
    n += 1;
  }
}

console.log(p / arr.length);
console.log(n / arr.length);
console.log(z / arr.length);
