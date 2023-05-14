const assert = require('assert').strict;
const calculateNumber = require('./0-calcul');

describe('testCaclculator', () =>{
  it('1 + 3', () =>{
    const PEPE = calculateNumber(1, 3)
    assert.equal(PEPE, 4);
  })
})