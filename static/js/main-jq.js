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
});
