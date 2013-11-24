$(document).on('ready', function(){
	$('input:submit').on('click', function(event){
		event.preventDefault();
		$.ajax({
			type: 'POST',
			url: '/login',
			data: {user: $("input:text").val(),
				   password: $("input:password").val()}
		}).done(function(data){
			$('#error-message').removeClass();
			if (data.url) {
				window.location.replace(data.url);
			}else{
				$('#error-message').empty();
				$('#error-message').append(data.html);
				$('#error-message').slideDown(function(){
					$('#error-message').css('display', 'inline-block');
				});
				$('#error-message').addClass('alert-danger');
			}
		});
	});
});