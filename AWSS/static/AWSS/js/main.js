(function ($)
  { "use strict"
    window.addEventListener('load', function() {
      // Check if the preloader has been shown before using localStorage
      if (!localStorage.getItem('preloaderShown')) {
          // Play video for 8 seconds, then fade out and display the home page
          setTimeout(function() {
              const preloader = document.getElementById('preloader-active');
              preloader.style.transition = 'opacity 1s ease';
              preloader.style.opacity = '0';  // Fade out
              setTimeout(function() {
                  preloader.style.display = 'none';  // After fade-out, hide the preloader
                  // Mark the preloader as shown in localStorage
                  localStorage.setItem('preloaderShown', 'true');
              }, 2000); // 2 second fade out
          }, 5000);  // Video plays for 5 seconds before fade
      } else {
          // If preloader has already been shown, just hide it immediately
          document.getElementById('preloader-active').style.display = 'none';
      }
  });
  $(window).on('scroll', function () {
    var scroll = $(window).scrollTop();
    if (scroll < 400) {
      $(".header-sticky").removeClass("sticky-bar");
      $('#back-top').hide(); // Instantly hide the #back-top element
    } else {
      $(".header-sticky").addClass("sticky-bar");
      $('#back-top').show(); // Instantly show the #back-top element
    }
  });
  
  // Scroll Up
  $('#back-top a').on("click", function () {
    $('body,html').animate({
      scrollTop: 0
    }, 800);
    return false;
  });
 /* 3. slick Nav */
 // mobile_menu
  var menu = $('ul#navigation');
  if(menu.length){
    menu.slicknav({
      prependTo: ".mobile_menu",
      closedSymbol: '+',
      openedSymbol:'-'
    });
  };    
   /* 4. MainSlider-1 */
    // h1-hero-active
    function mainSlider() {
      var BasicSlider = $('.slider-active');
      BasicSlider.on('init', function (e, slick) {
        var $firstAnimatingElements = $('.single-slider:first-child').find('[data-animation]');
        doAnimations($firstAnimatingElements);
      });
      BasicSlider.on('beforeChange', function (e, slick, currentSlide, nextSlide) {
        var $animatingElements = $('.single-slider[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
        doAnimations($animatingElements);
      });
      BasicSlider.slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: true,
        fade: true,
        arrows: false, 
        prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
        nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
        responsive: [{
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 991,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows: false
            }
          },
          {
            breakpoint: 767,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows: false,
              dots:false
            }
          }
        ]
      });

      function doAnimations(elements) {
        var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        elements.each(function () {
          var $this = $(this);
          var $animationDelay = $this.data('delay');
          var $animationType = 'animated ' + $this.data('animation');
          $this.css({
            'animation-delay': $animationDelay,
            '-webkit-animation-delay': $animationDelay
          });
          $this.addClass($animationType).one(animationEndEvents, function () {
            $this.removeClass($animationType);
          });
        });
      }
    }
    mainSlider();

    $('.owl-carousel').owlCarousel({
      autoplay: true,
      center: true,
      loop: true,
      nav: true,
      items:1
    });
 /* 5. Testimonial Active*/
  var testimonial = $('.h1-testimonial-active');
  if(testimonial.length){
  testimonial.slick({
    dots: true,
    infinite: true,
    speed: 1000,
    autoplay:false,
    arrows: false,
    prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
    slidesToShow: 1,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
          arrow:true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          dots: false,
          arrow:true
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          dots: false,
          arrow:true
        }
      }
    ]
  });
 }

 /* 6. Nice Selectorp  */
  var nice_Select = $('select');
  if(nice_Select.length){
    nice_Select.niceSelect();
  }

 /* 7. data-background */
  $("[data-background]").each(function () {
    $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
  });


 /* 10. WOW active */
  new WOW().init();

 // 11. ---- Mailchimp js --------//  
  function mailChimp() {
    $('#mc_embed_signup').find('form').ajaxChimp();
  }
  mailChimp();


 // 12 Pop Up Img
  var popUp = $('.single_gallery_part, .img-pop-up');
  if(popUp.length){
    popUp.magnificPopup({
      type: 'image',
      gallery:{
        enabled:true
      }
    });
  }
 // 12 Pop Up Video
  var popUp = $('.popup-video');
  if(popUp.length){
    popUp.magnificPopup({
      type: 'iframe'
    });
  }

 /* 13. counterUp*/
  $('.counter').counterUp({
    delay: 10,
    time: 3000
  });

 /* 14. Datepicker */
  $('#datepicker1').datepicker();

 // 15. Time Picker
  $('#timepicker').timepicker();

 //16. Overlay
  $(".snake").snakeify({
    speed: 200
  });


 //17.  Progress barfiller

  $('#bar1').barfiller();
  $('#bar2').barfiller();
  $('#bar3').barfiller();
  $('#bar4').barfiller();
  $('#bar5').barfiller();
  $('#bar6').barfiller();

})(jQuery);

