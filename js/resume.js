let zoomImages = (className) => {
    $(`.${className}`).unbind("click").on("click", function () {
        $("#div-zoom-area").css("display", "block");
        $("#img-zoom-area-content").attr("src", $(this)[0].src);

        $("#div-zoom-area").on("click", function () {
            $(this).css("display", "none");
        });
    });
};

/*!
    * Start Bootstrap - Resume v6.0.1 (https://startbootstrap.com/template-overviews/resume)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE)
    */
(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $("a.js-scroll-trigger[href*='#']:not([href='#'])").click(function () {
        if (location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate({
                    scrollTop: (target.offset().top)
                }, 100, "easeInOutExpo");
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#sideNav",
    });

    // Zoom images that have class name: img-zoomable
    zoomImages("img-zoomable");
})(jQuery); // End of use strict
