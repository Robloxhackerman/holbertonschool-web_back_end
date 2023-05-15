const expect = require('chai').expect;
const calculateNumber = require('./1-calcul');

describe('testCalculatorOmega', () => {
  describe('aaa', () => {
    it('SUM, 1.4, 4.5', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('SUM, 1.4, 4.5', () => {
      expect(calculateNumber('SUM', 5, 4.5)).to.equal(10);
    });
  });

  describe('aaa', () => {
    it('DIVIDE, 1.4, 4.5', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
  });

  describe('aaa', () => {
    it('SUBTRACT, 1.4, 4.5', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
  });

  describe('aaa', () => {
    it('DIVIDE, 1.4, 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error')
    });
  });

});