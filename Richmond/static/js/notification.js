$('.showContent').each(function(index) {
	$(this).on('click', function() {
		$('.notifContent:eq(' + index + ')').toggle(200);
	});
});

function setIsRead() {
	
}