const expect = require('chai').expect;
const calculateNumber = require('./1-calcul');

describe('testCalculatorOmega', () => {
  describe('aaa', () => {
    it('SUM, 1.4, 4.5', () => {
      const PEPE = calculateNumber('SUM', 1.4, 4.5);
      expect(PEPE).to.equal(6);
    });
  })

  it('DIVIDE, 1.4, 4.5', () => {
    const PEPE = calculateNumber('DIVIDE', 1.4, 4.5);
    expect(PEPE).to.equal(0.2);
  });
  it('SUBTRACT, 1.4, 4.5', () => {
    const PEPE = calculateNumber('SUBTRACT', 1.4, 4.5);
    expect(PEPE).to.equal(-4);
  });
  it('DIVIDE, 1.4, 0', () => {
    const PEPE = calculateNumber('DIVIDE', 1.4, 0);
    expect(PEPE).to.equal('Error')
  });
});