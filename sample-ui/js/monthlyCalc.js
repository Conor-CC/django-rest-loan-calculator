$(document).ready(() => {
    $('#range-1').on('input', function(){
      $('#monthly-principal-input').val($('#range-1').val());
    });

    $('#monthly-principal-input').on('keyup change', function(){
      $('#range-1').val($('#monthly-principal-input').val());
    });

    $('#monthly-principal-submit').on('click', function(){

      $('#monthly-results-pane').attr('class', 'd-none');
      $('#monthly-starter-pane').attr('class', 'd-none');
      $('#monthly-spinner').attr('class', 'card-body');

      function showResults() {
        $('#monthly-spinner').attr('class', 'd-none');

        $('#monthly-results-pane').attr('class', 'card-body');

        $('#monthly-pv-used').html($('#range-1').val());
        $('#monthly-np-used').html($('#period-1').val());
      }

      setTimeout(showResults, 350)
    });
});
