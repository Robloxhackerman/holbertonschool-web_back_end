var chai = require('chai');
const calculateNumber = require('./1-calcul');

describe('testCalculatorOmega', () => {
  describe('SUM no Round', () => {
    it('should return 5', () => {
      chai.expect(calculateNumber('SUM', 1, 4)).to.equal(5);
    });
  });

  describe('SUM first round', () => {
    it('should return 6', () => {
      chai.expect(calculateNumber('SUM', 2.4, 4)).to.equal(6);
    });
  });

  describe('SUM second round ', () => {
    it('should return 6', () => {
      chai.expect(calculateNumber('SUM', 4, 2.4)).to.equal(6);
    });
  });

  describe('SUM both round', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  });

  describe('SUBTRACT no round', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
    });
  });

  describe('SUBTRACT first round', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('SUBTRACT', 2, 4.5)).to.equal(-3);
    });
  });

  describe('SUBTRACT second round', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('SUBTRACT', 4.5, 2)).to.equal(3);
    });
  });

  describe('SUBTRACT both round', () => {
    it('aaaa', () => {
      chai.expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
  });

  describe('DIVIDE no round', () => {
    it('aaaa', () => {
      chai.expect(calculateNumber('DIVIDE', 8, 4)).to.equal(2);
    });
  });

  describe('DIVIDE first round', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('DIVIDE', 9.5, 2)).to.equal(5);
    });
  });

  describe('DIVIDE second round', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('DIVIDE', 2, 9.5)).to.equal(0.2);
    });
  });

  describe('DIVIDE both round', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
  });

  describe('DIVIDE Error', () => {
    it('aaa', () => {
      chai.expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });

});