export default function updateStudentGradeByCity(students, city, newGrades) {
  return (students.filter((item) => item.location === city)).map((info) => {
    const hasGrade = newGrades.filter((item) => item.studentId === info.id);
    if (hasGrade.length) {
      return { ...info, grade: hasGrade[0].grade };
    }
    return { ...info, grade: 'N/A' };
  });
}
