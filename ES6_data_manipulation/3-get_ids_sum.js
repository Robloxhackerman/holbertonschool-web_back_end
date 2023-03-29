export default function getStudentIdsSum(students) {
  return students.reduce((accumulator, item) => accumulator + item.id, 0);
}