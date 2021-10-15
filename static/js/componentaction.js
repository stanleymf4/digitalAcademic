(function($) {
  $("select[name=service_id]").focus(function(event){
    event.preventDefault();
    $(this).data('val', $(this).val());
    // alert($(this).data('val'));
  });

  $("select[name=service_component_group_id]").focus(function(event){
    event.preventDefault();
    $(this).data('val', $(this).val());
    // alert($(this).data('val'));
  });

  $("select[name=service_component_section_id]").focus(function(event){
    event.preventDefault();
    $(this).data('val', $(this).val());
    // alert($(this).data('val'));
  });

  $("select[name=service_id]").change(function(event) {
    // event.preventDefault();
    
    var prev = $(this).data('val');
    var current = $(this).val();
    if (prev != undefined) {
      $.ajax({
          url: '/request/data_mainsection',
          type: 'get',
          dataType:'json',
          data: {
            'service_id': $(this).val()
          },
          success : function(response) {
            var select =  $("select[name=service_component_group_id]");
            select.empty();
            let lenghtData = 0;
            JSON.parse(response).forEach(e => {
              lenghtData += 1
            });
            
            var optionNull = document.createElement("option");
            optionNull.value = ''
            optionNull.text= '---------'
            select.append(optionNull)
            
            for(let i = 0; i < lenghtData; i++) {
              var option = document.createElement("option");
              option.value = JSON.parse(response)[i].pk;
              option.text = JSON.parse(response)[i].fields.description
              select.append(option)
            }
          },
          error: function(response) {
            console.log(response);
          }
      });
    }
    
  });

  $("select[name=service_component_group_id]").change(function(event) {
    // event.preventDefault();
    
    var prev = $(this).data('val');
    var current = $(this).val();
    if (prev != undefined) {
      $.ajax({
          url: '/request/data_sections',
          type: 'get',
          dataType:'json',
          data: {
            'service_component_group_id': $(this).val()
          },
          success : function(response) {
            var select =  $("select[name=service_component_section_id]");
            select.empty();
            let lenghtData = 0;
            JSON.parse(response).forEach(e => {
              lenghtData += 1
            });
            
            var optionNull = document.createElement("option");
            optionNull.value = ''
            optionNull.text= '---------'
            select.append(optionNull)
            
            for(let i = 0; i < lenghtData; i++) {
              var option = document.createElement("option");
              option.value = JSON.parse(response)[i].pk;
              option.text = JSON.parse(response)[i].fields.description
              select.append(option)
            }
          },
          error: function(response) {
            console.log(response);
          }
      });
    }
    
  });
})(django.jQuery);
