$('.showContent').each(function(index) {
	$(this).on('click', function() {
		$('.notifContent:eq(' + index + ')').toggle(200);
	});
});

function setIsRead(notif_id) {
	$.ajax({
		url: '/readNotification/',
		type: 'POST',
		data: {'id': notif_id},
		success: function(response) {
			$('#unread' + notif_id).css('display', 'none');
		}
	});
}