export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a String');
    if (typeof length !== 'number') throw TypeError('Length must be a Number');
    if (students.constructor !== Array && students.every((element) => typeof element === 'string')) throw TypeError('students must be an Array of Strings');

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value === 'string') {
      this._name = value;
    } else {
      throw TypeError('Name must be a String');
    }
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value === 'number') {
      this._length = value;
    } else {
      throw TypeError('Length must be a Number')
    }
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (value.constructor === Array && value.every((element) => typeof element === 'string')) {
      this._students = value;
    } else {
      throw TypeError('students must be an Array of Strings')
    }
  }
}
