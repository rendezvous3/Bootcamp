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

	$(".btn-post").click(function() {
		//console.log($(".form-control").val())
		$.ajax({
	      url: '/post/',
	      data: $("#compose-form").serialize(),
	      type: 'post',
	      cache: false,
	      success: function (data) {
	        $("ul.stream").prepend(data);
	        $(".compose").slideUp();
	      }
	    });
	})
});

