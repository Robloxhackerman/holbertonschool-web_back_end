const expect = require('chai').expect;
const sinon = require("sinon");
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () =>{
  const spyConsole = sinon.spy(console, 'log');

  it('aaaa', () => {
    sendPaymentRequestToApi(100, 20);
    const stubUtils = sinon.stub(Utils, 'calculateNumber');
    stubUtils.withArgs('SUM', 100, 20).returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(spyConsole.calledOnce).to.be.true;
    expect(spyConsole.calledWith('The total is: 10')).to.be.true;
    stubUtils.restore()
    spyConsole.restore();
  });
});