$(document).ready(function() {
"use strict";

// Menu Scroll
$('.menu li > a').click(function(event) {
    $('.menu li > a').removeClass('active');
    $(this).addClass('active');
    $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top }, 2000);
    event.preventDefault();
});

});