export default function createIteratorObject(report) {
  const empleados = [];
  /* eslint-disable*/
  for (const [department, employees] of Object.entries(report.allEmployees)) {
    for (const employe of employees) {
      empleados.push(employe);
    }
  }
  /* eslint-enable*/

  return empleados;
}
