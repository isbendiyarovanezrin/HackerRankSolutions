// Language: JavaScript (Node.js)

function vowelsAndConsonants(s) {
  let vowels = [];
  let consonants = [];
  for (let i = 0; i < s.length; i++) {
    if (
      s[i] === "a" ||
      s[i] === "e" ||
      s[i] === "i" ||
      s[i] === "o" ||
      s[i] === "u"
    ) {
      vowels.push(s[i]);
    } else {
      consonants.push(s[i]);
    }
  }
  let c = vowels.concat(consonants);
  let j = c.join("\n");
  console.log(j);
}
