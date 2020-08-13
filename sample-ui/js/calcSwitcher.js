$(document).ready(() => {

  $('#dropdown-menu').on('show.bs.dropdown', function () {
    $('[data-toggle-second="tooltip"]').tooltip('hide')
    $('#content-window').attr('style', 'filter: blur(4px); -webkit-filter: blur(4px);');
  });

  $('#dropdown-menu').on('hide.bs.dropdown', function () {
    $('#content-window').attr('style', '');
  });

  $('#monthly-repayment-selector').on('click', function(){
    let attr = $("#monthly-repayment-content").attr("class");
    if (attr.indexOf("d-none") > -1) {
      $("#calc-selector").html("Monthly Repayments Calculator");

      $("#monthly-repayment-selector").attr("class","dropdown-item active");
      $("#repayment-count-selector").attr("class","dropdown-item");
      $("#interest-rate-selector").attr("class","dropdown-item");

      $("#monthly-repayment-content").attr("class","row");
      $("#repayment-count-content").attr("class","row d-none");
      $("#interest-rate-content").attr("class","row d-none");
    }
  });

  $('#repayment-count-selector').on('click', function(){
    let attr = $("#repayment-count-content").attr("class");
    if (attr.indexOf("d-none") > -1) {
      $("#calc-selector").html("Repayment Periods Calculator");

      $("#repayment-count-selector").attr("class","dropdown-item active");
      $("#monthly-repayment-selector").attr("class","dropdown-item");
      $("#interest-rate-selector").attr("class","dropdown-item");

      $("#repayment-count-content").attr("class","row");
      $("#monthly-repayment-content").attr("class","row d-none");
      $("#interest-rate-content").attr("class","row d-none");
    }
  });

  $('#interest-rate-selector').on('click', function(){
    let attr = $("#interest-rate-content").attr("class");
    if (attr.indexOf("d-none") > -1) {
      $("#calc-selector").html("Interest Rate Calculator");

      $("#interest-rate-selector").attr("class","dropdown-item active");
      $("#monthly-repayment-selector").attr("class","dropdown-item");
      $("#repayment-count-selector").attr("class","dropdown-item");

      $("#interest-rate-content").attr("class","row");
      $("#monthly-repayment-content").attr("class","row d-none");
      $("#repayment-count-content").attr("class","row d-none");
    }
  });
});
