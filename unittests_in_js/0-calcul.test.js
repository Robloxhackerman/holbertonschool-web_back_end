const assert = require('assert').strict;
const calculateNumber = require('./0-calcul');

describe('testCaclculator', () =>{
  it('1 + 3', () =>{
    const PEPE = calculateNumber(1, 3);
    assert.equal(PEPE, 4);
  });

  it('1 + 3.7', () => {
    const PEPE = calculateNumber(1, 3.7);
    assert.equal(PEPE, 5);
  });

  it('1.2, 3.7', () => {
    const PEPE = calculateNumber(1.2, 3.7);
    assert.equal(PEPE, 5)
  });

  it('1.5, 3.1', () => {
    const PEPE = calculateNumber(1.5, 3.1);
    assert.equal(PEPE, 5)
  });
});