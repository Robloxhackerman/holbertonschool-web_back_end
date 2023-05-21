const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('testCalculatorOmega', () => {
  it('SUM, 1.4, 4.5', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('SUM, 1.4, 4.5', () => {
    expect(calculateNumber('SUM', 5, 4.5)).to.equal(10);
  });

  it('DIVIDE, 1.4, 4.5', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });

  it('SUBTRACT, 1.4, 4.5', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('DIVIDE, 1.4, 0', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error')
  });

});