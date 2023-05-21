const fs = require('fs');

function countStudents(ruta) {
  return new Promise((resolve, reject) => {
    fs.readFile(ruta, (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      const res = [];
      let msg;
      const content = data.toString().split('\n');
      let students = content.filter((item) => item);

      students = students.map((item) => item.split(','));

      const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
      msg = (`Number of students: ${NUMBER_OF_STUDENTS}`);
      console.log(msg);

      res.push(msg);

      const fields = {};
      for (const PEPE in students) {
        if (PEPE !== 0) {
          if (!fields[students[PEPE][3]]) fields[students[PEPE][3]] = [];

          fields[students[PEPE][3]].push(students[PEPE][0]);
        }
      }

      delete fields.field;

      for (const key of Object.keys(fields)) {
        msg = (`Number of students in ${key}: ${
          fields[key].length
        }. List: ${fields[key].join(', ')}`);

        console.log(msg);

        res.push(msg);
      }
      resolve(res);
    });
  });
}

module.exports = countStudents;
