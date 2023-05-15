const assert = require('assert').strict;
const calculateNumber = require('./1-calcul');

describe('testCalculatorOmega', () => {
  it('SUM, 1.4, 4.5', () => {
    const PEPE = calculateNumber('SUM', 1.4, 4.5);
    assert.equal(PEPE, 6)
  });
  it('DIVIDE, 1.4, 4.5', () => {
    const PEPE = calculateNumber('DIVIDE', 1.4, 4.5);
    assert.equal(PEPE, 0.2)
  });
  it('SUBTRACT, 1.4, 4.5', () => {
    const PEPE = calculateNumber('SUBTRACT', 1.4, 4.5);
    assert.equal(PEPE, -4)
  });
  it('DIVIDE, 1.4, 0', () => {
    const PEPE = calculateNumber('DIVIDE', 1.4, 0);
    assert.equal(PEPE, 'Error');
  });
});