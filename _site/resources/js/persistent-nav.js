$(function() {
	var nav = $("#nav-container"), pos = nav.offset();
	var content = $("#content");
	$(window).scroll(function() { 
		if($(this).scrollTop() > (pos.top) &&
			nav.css('position') == 'static') { 
			nav.addClass('fixed');  
			content.addClass('bumped');  
		} else if($(this).scrollTop() <= pos.top &&
			nav.hasClass('fixed')) { 
			nav.removeClass('fixed'); 
			content.removeClass('bumped');  
		}
	})
});
