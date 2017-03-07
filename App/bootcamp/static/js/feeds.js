$(function () {
	$(".btn-page-header").click(function() {
		$(".compose textarea").val("");
		$(".compose").slideDown(400, function(){
			$(".compose textarea").focus()
		});
	});

	$(".btn-cancel-compose").click(function () {
		$(".compose").slideUp()
	})
});

