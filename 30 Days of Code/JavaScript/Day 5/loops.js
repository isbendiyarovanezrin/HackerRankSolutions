// Language: JavaScript (Node.js)

function main() {
  const n = parseInt(readLine().trim(), 10);
  for (let i = 1; i <= 10; i++) {
    let s = n * i;
    console.log(`${n} x ${i} = ${s}`);
  }
}
