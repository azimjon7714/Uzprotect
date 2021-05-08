$(document).ready(function(){
	$('a[data-target^="anchor"]').bind('click.smoothscroll', function(){
		var target = $(this).attr('href'),
			margin_top = $(target).offset().top - 100;

		$('body, html').animate({scrollTop: margin_top}, 1200);
		return false;
	});
});