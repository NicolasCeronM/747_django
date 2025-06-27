console.log([...document.querySelectorAll(".add-to-cart")].length);

document.addEventListener("DOMContentLoaded", function () {
  const productCards = document.querySelectorAll(".product-card");

  productCards.forEach((card) => {
    const wrappers = card.querySelectorAll(".product-images .lazy-img-wrapper");
    const indicators = card.querySelectorAll(".image-indicators .indicator");
    let currentIndex = 0;
    let interval;

    // =============== ROTACIÓN DE IMÁGENES (HOVER) ===============
    card.addEventListener("mouseenter", () => {
      if (wrappers.length <= 1) return;
      interval = setInterval(() => {
        wrappers[currentIndex].classList.remove("active");
        indicators[currentIndex].classList.remove("active");

        currentIndex = (currentIndex + 1) % wrappers.length;
        wrappers[currentIndex].classList.add("active");
        indicators[currentIndex].classList.add("active");
      }, 1000);
    });

    card.addEventListener("mouseleave", () => {
      clearInterval(interval);
      wrappers.forEach((wrap, index) =>
        wrap.classList.toggle("active", index === 0)
      );
      indicators.forEach((ind, index) =>
        ind.classList.toggle("active", index === 0)
      );
      currentIndex = 0;
    });

    indicators.forEach((indicator, index) => {
      indicator.addEventListener("click", (e) => {
        e.stopPropagation();
        clearInterval(interval);
        wrappers.forEach((wrap) => wrap.classList.remove("active"));
        indicators.forEach((ind) => ind.classList.remove("active"));
        wrappers[index].classList.add("active");
        indicator.classList.add("active");
        currentIndex = index;
      });
    });

    // =============== TALLA SELECCIONADA ===============
    const sizeButtons = card.querySelectorAll(".size-btn");
    sizeButtons.forEach((button) => {
      button.addEventListener("click", function () {
        sizeButtons.forEach((b) => b.classList.remove("selected"));
        this.classList.add("selected");
      });
    });

    // =============== AGREGAR AL CARRITO (AJAX) ===============
    const addToCartBtn = card.querySelector(".add-to-cart");

    if (!addToCartBtn.dataset.bound) {
      addToCartBtn.dataset.bound = true;

      addToCartBtn.addEventListener("click", function () {
        const productId = card.dataset.productId;
        const selectedSizeBtn = card.querySelector(".size-btn.selected");
        const selectedSize = selectedSizeBtn
          ? selectedSizeBtn.dataset.size
          : null;

        if (!productId || productId === "undefined") {
          console.error("ID de producto no definido");
          return;
        }

        if (!selectedSize) {
          Swal.fire({
            icon: "warning",
            title: "Selecciona una talla",
            text: "Debes elegir una talla antes de agregar al carrito",
          });
          return;
        }

        const originalText = this.textContent;
        this.textContent = "✓ Agregado";
        setTimeout(() => {
          this.textContent = originalText;
        }, 1500);

        fetch("/cart/add-ajax/", {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken"),
          },
          body: new URLSearchParams({
            product_id: productId,
            size: selectedSize,
            quantity: 1,
          }),
        })
          .then((response) => {
            if (!response.ok) {
              if (response.status === 403) {
                Swal.fire({
                  icon: "warning",
                  title: "Inicia sesión",
                  text: "Debes iniciar sesión para agregar productos al carrito.",
                });
                return;
              } else {
                throw new Error("Error HTTP: " + response.status);
              }
            }
            return response.json();
          })
          .then((data) => {
            if (!data) return;
            if (data.success) {
              const cartCount = document.getElementById("cart-count");
              if (cartCount) {
                cartCount.textContent = data.total_items;
                cartCount.classList.remove("d-none");
              }

              Swal.fire({
                toast: true,
                position: "top-end",
                icon: "success",
                title: "Producto agregado al carrito",
                showConfirmButton: false,
                timer: 1800,
                timerProgressBar: true,
              });
            } else {
              Swal.fire({
                icon: "error",
                title: "Error",
                text: data.message,
              });
            }
          })
          .catch((error) => {
            console.error("Error en la solicitud AJAX:", error);
            Swal.fire({
              icon: "error",
              title: "Error inesperado",
              text: "Ocurrió un error al agregar el producto.",
            });
          });
      });
    }
  });
});

// =============== TOKEN CSRF PARA POST ===============
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
  const productCards = document.querySelectorAll(".product-card");

  productCards.forEach((card) => {
    const wrappers = card.querySelectorAll(".product-images .lazy-img-wrapper");
    const indicators = card.querySelectorAll(".image-indicators .indicator");
    let currentIndex = 0;
    let interval;

    // Rotación automática de imágenes al pasar el mouse
    card.addEventListener("mouseenter", () => {
      if (wrappers.length <= 1) return;
      interval = setInterval(() => {
        wrappers[currentIndex].classList.remove("active");
        indicators[currentIndex].classList.remove("active");

        currentIndex = (currentIndex + 1) % wrappers.length;
        wrappers[currentIndex].classList.add("active");
        indicators[currentIndex].classList.add("active");
      }, 1000);
    });

    card.addEventListener("mouseleave", () => {
      clearInterval(interval);
      wrappers.forEach((wrap, index) =>
        wrap.classList.toggle("active", index === 0)
      );
      indicators.forEach((ind, index) =>
        ind.classList.toggle("active", index === 0)
      );
      currentIndex = 0;
    });

    // Rotación manual al hacer clic en los indicadores
    indicators.forEach((indicator, index) => {
      indicator.addEventListener("click", (e) => {
        e.stopPropagation();
        clearInterval(interval);
        wrappers.forEach((wrap) => wrap.classList.remove("active"));
        indicators.forEach((ind) => ind.classList.remove("active"));
        wrappers[index].classList.add("active");
        indicator.classList.add("active");
        currentIndex = index;
      });
    });
  });

  // Cargar las imágenes reales (lazy loading)
  cargarImagenesLazy();
});

// Función que reemplaza las siluetas por la imagen real
function cargarImagenesLazy() {
  const lazyWrappers = document.querySelectorAll(".lazy-img-wrapper");

  lazyWrappers.forEach((wrapper) => {
    const img = wrapper.querySelector("img.lazy-img");
    const realSrc = img.dataset.src;

    if (img.classList.contains("loaded")) return;

    const loader = new Image();
    loader.src = realSrc;

    loader.onload = function () {
      img.src = realSrc;
      img.classList.add("loaded");
      wrapper.classList.add("loaded");
    };
  });
}
