// Initialize carousel with auto-scrolling
document.addEventListener("DOMContentLoaded", function () {
  const myCarousel = new bootstrap.Carousel(
    document.getElementById("mainCarousel"),
    {
      interval: 5000, // Change slide every 5 seconds
      pause: "hover", // Pause on hover
      wrap: true, // Continuously loop
    }
  );
});
