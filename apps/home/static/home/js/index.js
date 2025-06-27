document.addEventListener("DOMContentLoaded", function () {
  const lazyWrappers = document.querySelectorAll(".lazy-img-wrapper");

  lazyWrappers.forEach((wrapper) => {
    const img = wrapper.querySelector("img.lazy-img");
    const realSrc = img.dataset.src;

    const loader = new Image();
    loader.src = realSrc;

    loader.onload = function () {
      img.src = realSrc;
      img.classList.add("loaded");
      wrapper.classList.add("loaded");
    };
  });
});
