//SIDEBAR TOGGLE

$(function() {
	$(".toggle-sidebar").click(function () {
	  $('body').toggleClass("show-sidebar");
	});

	var contentMinHeight 	= $('.sidebar .wrapper').height();
	var frameMinHeight 		= $( document ).height();

	$('.frame').css('min-height', frameMinHeight);
	$('.content').css('min-height', contentMinHeight);
});





//TEXTAREA AUTOSIZE
$(function(){
	//$('.autosize-normal').autosize();
	//WYSIHTML5
	if($('#textarea').length > 0)
	{
		var editor = new wysihtml5.Editor("textarea", {
			toolbar:      "toolbar",
			stylesheets:  STATIC_URL+"css/theme-editor.css"
		});
	}
});