$(document).ready(() => {
    $('#range-1').on('input', function(){
      $('#monthly-principal-input').val($('#range-1').val());
    });

    $('#monthly-principal-input').on('keyup change', function(){
      $('#range-1').val($('#monthly-principal-input').val());
    });

    $('#monthly-principal-submit').on('click', function(){
      $('#monthly-results-pane').attr('class', 'card-body');
      $('#monthly-starter-pane').attr('class', 'card-body d-none');

      $('#monthly-pv-used').html($('#range-1').val());
      $('#monthly-np-used').html($('#period-1').val());
    });
});
