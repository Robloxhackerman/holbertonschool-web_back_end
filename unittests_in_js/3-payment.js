const Utils = require('./utils.js')
function sendPaymentRequestToApi(totalAmount, totalShipping){
  console.log(Utils.calculateNumber('SUM', totalAmount, totalShipping));
}

module.exports = sendPaymentRequestToApi;