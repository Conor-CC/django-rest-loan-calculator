$(document).ready(() => {

    $('#repayment-range').on('input', function(){
      $('#repayment-principal-input').val($('#repayment-range').val());
    });

    $('#repayment-principal-input').on('keyup change', function(){
      $('#repayment-range').val($('#repayment-principal-input').val());
    });

    $('#repayment-principal-submit').on('click', function(){

      $('#repayment-results-pane').attr('class', 'd-none');
      $('#repayment-starter-pane').attr('class', 'd-none');
      $('#repayment-spinner').attr('class', 'card-body');

      function showResults() {
        $('#repayment-spinner').attr('class', 'd-none');

        $('#repayment-results-pane').attr('class', 'card-body');

        $('#repayment-pv-used').html($('#repayment-range').val());
        $('#repayment-mr-used').html($('#monthly-repayment-val').val());
      }

      setTimeout(showResults, 350)

    });
});
