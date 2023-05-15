const expect = require('chai').expect;
const calculateNumber = require('./1-calcul');

describe('testCalculatorOmega', () => {
  describe('aaa', () => {
    it('SUM, 1.4, 4.5', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  })

  describe('aaa', () => {
    it('DIVIDE, 1.4, 4.5', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
  });

  it('SUBTRACT, 1.4, 4.5', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('DIVIDE, 1.4, 0', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error')
  });
});