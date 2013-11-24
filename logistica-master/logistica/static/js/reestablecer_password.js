$(document).on('ready', function(){
	$('input:submit').on('click', function(event){
		event.preventDefault();

		$.ajax({
			type: "POST",
			url: "/validar_usuario",
			data: { user: $('input:text').val()}
		}).done(function(data, statusText, xhr){
			$('#error-message').removeClass();
			$('#error-message').empty();
			$('#error-message').append(data.html);
			$('#error-message').slideDown(function(){
				$('#error-message').css('display', 'inline-block');	
			});
			if (data.url) {
				$('#error-message').addClass('alert-success');
				setTimeout(function(){
					window.location.replace(data.url);
				}, 7000);
			}else{
				$('#error-message').addClass('alert-danger');
			}
			
		});
	});
});