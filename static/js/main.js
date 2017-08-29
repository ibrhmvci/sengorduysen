$(document).ready(function () {
    $('#main-slider').owlCarousel({
        loop:true,
        margin:10,
        items:1,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
                nav:true
            },
            600:{
                items:1,

            },
            1000:{
                items:1,
            }
        }
    });
    // Logo carousel JS
    $('#logo-carousel').owlCarousel({
        loop:true,
        margin:10,
        items:1,
        responsiveClass:true,
        responsive:{
            0:{
                items:2,
                nav:true
            },
            600:{
                items:3

            },
            1000:{
                items:5
            }
        }
    });

});