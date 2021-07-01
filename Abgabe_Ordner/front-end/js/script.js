
$('#profile_div').click(function () {
	$('.profile_div').toggle();
	$('.content').toggle();
});

$('#close').click(function () {
	$('.profile_div').toggle();
	$('.content').toggle();
});


function newMessage() {
	message = $(".message-input input").val();
	if($.trim(message) == '') {
		return false;
	}
	$('<li class="sent"><img src="images/user_icon.png" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
	$('.message-input input').val(null);  
  send(message);
};

$('.submit').click(function() {
  newMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    newMessage();
    return false;
  }
});



function send(message) {
	console.log("User Message:", message)
	$.ajax({
		url: 'http://localhost:5005/webhooks/rest/webhook',
		type: 'POST',
		contentType: 'application/json',
		data: JSON.stringify({
			"message": message,
			"sender": "Me"
		}),
		success: function (data, textStatus) {
			if(data != null){
          setBotResponse(data);
			}
			console.log("Rasa Response: ", data, "\n Status:", textStatus)
		},
		error: function (errorMessage) {
			setBotResponse("");
			console.log('Error' + errorMessage);

		}
	});
}
function setBotResponse(val) {
	setTimeout(function () {
		if (val.length < 1) {
			msg = 'Entschuldigung, Ich hab dich nicht verstanden. könntest du deine Bitte genauer stellen?';

			$('<li class="replies"><img src="images/botAvatar.png" alt="" /><p>' + msg + '</p></li>').appendTo($('.messages ul'));

		} else {
			for (i = 0; i < val.length; i++) {
				if (val[i].hasOwnProperty("text")) {
					$('<li class="replies"><img src="images/botAvatar.png" alt="" /><p>' + val[i].text + '</p></li>').appendTo($('.messages ul'));
				}

				if (val[i].hasOwnProperty("image")) {
					$('<div class="singleCard"><img class="imgcard" src="' + val[i].image + '"></div>').appendTo($('.messages ul'));
				}
			}
		}

  }, 500);
}
