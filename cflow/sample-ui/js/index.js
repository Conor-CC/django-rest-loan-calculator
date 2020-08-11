$(document).ready(() => {
  //initial tasks
  $('#monthly-prinicipal-1').html($('#range-1').val());
  $('#monthly-principal-input').val($('#range-1').val());

  $('#repayment-range').val($('#repayment-principal-input').val());

  $('#interest-range').val($('#interest-principal-input').val());
});
