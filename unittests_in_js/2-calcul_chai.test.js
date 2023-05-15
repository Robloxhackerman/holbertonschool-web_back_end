const chai = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

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
      chai.expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error')
    });
  });

});