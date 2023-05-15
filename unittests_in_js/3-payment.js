const Utils = require('utils')
function sendPaymentRequestToApi(totalAmount, totalShipping){
  console.log(Utils.calculateNumber('SUM', totalAmount, totalShipping));
}

module.exports = sendPaymentRequestToApi;