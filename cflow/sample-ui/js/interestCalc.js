$(document).ready(() => {

    $('#interest-range').on('input', function(){
      $('#interest-principal-input').val($('#interest-range').val());
    });

    $('#interest-principal-input').on('keyup change', function(){
      $('#interest-range').val($('#interest-principal-input').val());
    });

    $('#interest-principal-submit').on('click', function(){



      $('#interest-results-pane').attr('class', 'card-body');
      $('#interest-starter-pane').attr('class', 'card-body d-none');

      $('#interest-pv-used').html($('#interest-range').val());
      $('#interest-np-used').html($('#interest-period-val').val());
      $('#interest-mr-used').html($('#interest-repayment-val').val());
    });
});
