export default function getStudentsByLocation(student, city) {
  return student.filter((item) => item.location === city);
}