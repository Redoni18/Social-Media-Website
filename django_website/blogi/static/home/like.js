$('#like_form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/like/<int:pk>/',
        type : 'POST',
        data : { 
            like : $('#like').val(),
            dislike : $('#dislike').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
         },

        success : function(){
            
    });
});