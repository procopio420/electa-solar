(function ($) {
    'use strict';

    // Testimonials Slides Active Code
    if ($.fn.owlCarousel) {
        $(".testimonials-slides").owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            smartSpeed: 1500,
            margin: 5,
            nav: true,
            navText: ['<i class="ti-angle-left"></i>', '<i class="ti-angle-right"></i>']
        })
    }
    
    // Search Btn Active Code
    $('#search-btn, #closeBtn').on('click', function () {
        $('body').toggleClass('search-form-on');
    });

    // Progress Bar Active Code
    if ($.fn.barfiller) {
        $('#bar1').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar2').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar3').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
        $('#bar4').barfiller({
            tooltip: true,
            duration: 1000,
            animateOnResize: true
        });
    }

    // ScrollUp Active Code
    if ($.fn.scrollUp) {
        $.scrollUp({
            scrollSpeed: 1500,
            scrollText: '<i class="fa fa-angle-up" aria-hidden="true"></i>'
        });
    }


    // Video Active Code
    if ($.fn.magnificPopup) {
        $('.video--play--btn').magnificPopup({
            disableOn: 0,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: true,
            fixedContentPos: false
        });
    }

    // PreventDefault a Click
    $("a[href='#']").on('click', function ($) {
        $.preventDefault();
    });

    // wow Active Code
    if ($.fn.init) {
        new WOW().init();
    }

    // matchHeight Active Code
    if ($.fn.matchHeight) {
        $('.item').matchHeight();
    }

    var $window = $(window);

    // Preloader active code
    $window.on('load', function () {
        $('#preloader').fadeOut('slow', function () {
            $(this).remove();
        });
    });

})(jQuery);

$(document).ready(function(){
    document.getElementById('saving').innerHTML = 0;
    $('#area').on('input', function() { 
        var area = this.value;
        if(isNaN(area)){
            document.getElementById('labelSave').innerHTML = "The area has to be in meters. <b>Only numbers accepted!</b>";
        }
        else {
            var x = (area/10)*1750;
            var savings =  x * (1.15 - (1.15*0.9))*25;
            savings = Math.round(savings);
            document.getElementById('labelSave').innerHTML = 'You can save: <span style="font-weight: bolder;" id="saving">&times;</span> EGP per month';
            document.getElementById('saving').innerHTML = savings;
        }
        
    });
});
function openquote(){
    $('#calc').modal('hide');
    $('#calc').on('hidden.bs.modal', function(){
        $('#quote').modal('show');
        $('#quote').modal('handleUpdate');
    })
}
