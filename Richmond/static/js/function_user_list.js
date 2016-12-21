function follow() {
	// alert("您已跟注該用戶！\n\n請選擇跟注金額");
	// $.ajax({
	// 	url: '/follow/',
	// 	type: 'POST',
	// 	data: { 'follow_user': user }
	// });
}

function subscribe() {
	// alert("您已關注該用戶！");
	// $.ajax({
	// 	url: '/subscribe/',
	// 	type: 'POST',
	// 	data: { 'subscribe_user': user }
	// });
}

$('#mode').change(function() {
	modeId = $('#mode option:selected').val();
	$('.mode_desc').each(function() {
		$(this).css( 'display', 'none' );
	});
	$('#mode' + modeId + '_desc').css( 'display', 'block' );
});