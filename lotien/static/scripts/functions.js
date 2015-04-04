$(document).ready(function() {
"use strict";

  // Portfolio
  $('.portfolio .item a').click( function(event) {
    $('.items[data-group=' + $(this).data('group') + ']').slideToggle('slow');
    event.preventDefault();
  });

  $('.portfolio .items .close').click( function(event) {
    $(this).parent().slideUp();
    event.preventDefault();
  });

  // Imagelightbox
  var overlayOn = function() {
        $('<div id="imagelightbox-overlay"></div>').appendTo('body');
      },
      overlayOff = function() {
        $('#imagelightbox-overlay').remove();
      },
      closeButtonOn = function( instance ) {
        $('<a href="#" id="imagelightbox-close">Close</a>').appendTo('body').on('click', function(){ $( this ).remove(); instance.quitImageLightbox(); return false; });
      },
      closeButtonOff = function() {
        $('#imagelightbox-close').remove();
      },
      activityIndicatorOn = function() {
        $( '<div id="imagelightbox-loading"><div></div></div>' ).appendTo( 'body' );
      },
      activityIndicatorOff = function() {
        $( '#imagelightbox-loading' ).remove();
      };

  var instance = $( '.product a, .portfolio .items a' ).imageLightbox({
    onStart: function() { overlayOn(); closeButtonOn( instance ) },
    onEnd: function() { overlayOff(); closeButtonOff(); },
    onLoadStart: function() { activityIndicatorOn(); },
    onLoadEnd: function() { activityIndicatorOff(); }
  });

  // FlexSlider
  $('.promo .flexslider').flexslider({
    animation: "fade",
    directionNav: false,
    slideshowSpeed: 10000,
    animationSpeed: 800
  });

});
