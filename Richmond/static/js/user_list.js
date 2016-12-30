function subscribe(subscribee, id) {
	$.ajax({
		url: '/subscribe/',
		type: 'POST',
		data: { 'subscribee': subscribee },
		success: function(response) {
			alert("您已關注用戶" + subscribee + "!");
			$('#subscribe' + id).prop('disabled', true);
		}
	});
}

$('#mode').change(function() {
	modeId = $('#mode option:selected').val();
	$('.mode_desc').each(function() {
		$(this).css( 'display', 'none' );
	});
	$('#mode' + modeId + '_desc').css( 'display', 'block' );
});