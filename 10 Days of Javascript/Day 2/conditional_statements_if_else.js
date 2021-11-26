// Language: JavaScript (Node.js)

function getGrade(score) {
  let grade;
  if (0 <= score && score <= 5) {
    grade = "F";
  }
  if (5 < score && score <= 10) {
    grade = "E";
  }
  if (10 < score && score <= 15) {
    grade = "D";
  }
  if (15 < score && score <= 20) {
    grade = "C";
  }
  if (20 < score && score <= 25) {
    grade = "B";
  }
  if (25 < score && score <= 30) {
    grade = "A";
  }
  return grade;
}
