const expect = require('chai').expect;
const sinon = require("sinon");
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () =>{
  const spyUtils = sinon.spy(Utils, 'calculateNumber');

  it('aaaa', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyUtils.calledOnce).to.be.true;
    expect(spyUtils.calledWith('SUM', 100, 20)).to.be.true;
    spyUtils.restore()
  });
});