$(document).ready(() => {
  //initial tasks

  $(function () {
      $('[data-toggle-second="tooltip"]').tooltip({ delay: { "show": 2000, "hide": 500 }})
  })

  $('#monthly-prinicipal-1').html($('#range-1').val());
  $('#monthly-principal-input').val($('#range-1').val());

  $('#repayment-range').val($('#repayment-principal-input').val());

  $('#interest-range').val($('#interest-principal-input').val());
});
