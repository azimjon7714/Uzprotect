$(window).scroll(function () { 
    parallax();
})

function parallax() {

    var wScroll = $(window).scrollTop();

    $('.parallax--bg').css('background-position', 
    'center '+(wScroll)+'px')

    $('.footer-bg').css('background-position',
    'center '+(wScroll)+'px')
}

