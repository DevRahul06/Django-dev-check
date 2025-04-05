$(document).ready(function () {
  $(".home-slider").owlCarousel({
    items: 1, // Show one item at a time
    loop: true, // Enable infinite loop
    nav: false, // Show navigation buttons
    dots: false, // Hide dots
    autoplay: true, // Enable autoplay
    autoplayTimeout: 3000, // Auto-slide every 3 seconds
    autoplayHoverPause: true, // Pause on hover
  });
  // Custom navigation button events
  $(".home-next").click(function () {
    $(".home-slider").trigger("next.owl.carousel");
  });

  $(".home-prev").click(function () {
    $(".home-slider").trigger("prev.owl.carousel");
  });

  // Service Card Section Start
  $(".service-slider").owlCarousel({
    items: 3,
    margin: 10,
    loop: true,
    nav: false,
    dots: false,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    autoHeight: false,
    responsive: {
      0: {
        items: 1, // Show 1 item on small screens
      },
      767: {
        items: 1.5, // Show 2 items on tablets
      },

      1000: {
        items: 2, // Show 3 items on desktops
      },
      1200: {
        items: 3,
      },
    },
  });
  // Custom navigation button events
  $(".service-next").click(function () {
    $(".service-slider").trigger("next.owl.carousel");
  });

  $(".service-prev").click(function () {
    $(".service-slider").trigger("prev.owl.carousel");
  });


  // client-slider Section

  $(".client-slider").owlCarousel({
    items: 4,
    margin: 10,
    loop: true,
    nav: false,
    center: true, 
    dots: false,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    autoHeight: false,
    responsive: {
      0: {
        items: 1, // Show 1 item on small screens
      },
      767: {
        items: 1.5, // Show 2 items on tablets
      },

      1000: {
        items: 2, // Show 3 items on desktops
      },
      1200: {
        items: 4,
      },
    },
  });
  // Custom navigation button events
  $(".client-next").click(function () {
    $(".client-slider").trigger("next.owl.carousel");
  });

  $(".client-prev").click(function () {
    $(".client-slider").trigger("prev.owl.carousel");
  });
});
