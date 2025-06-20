console.log([...document.querySelectorAll(".add-to-cart")].length);
document.addEventListener("DOMContentLoaded", function () {
  const productCards = document.querySelectorAll(".product-card");

  productCards.forEach((card) => {
    const images = card.querySelectorAll(".product-images img");
    const indicators = card.querySelectorAll(".image-indicators .indicator");
    let currentIndex = 0;
    let interval;

    // Rotación de imágenes
    card.addEventListener("mouseenter", () => {
      if (images.length <= 1) return;
      interval = setInterval(() => {
        images[currentIndex].classList.remove("active");
        indicators[currentIndex].classList.remove("active");

        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].classList.add("active");
        indicators[currentIndex].classList.add("active");
      }, 1000);
    });

    card.addEventListener("mouseleave", () => {
      clearInterval(interval);
      images.forEach((img, index) =>
        img.classList.toggle("active", index === 0)
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
        images.forEach((img) => img.classList.remove("active"));
        indicators.forEach((ind) => ind.classList.remove("active"));
        images[index].classList.add("active");
        indicator.classList.add("active");
        currentIndex = index;
      });
    });

    // Botón de talla
    const sizeButtons = card.querySelectorAll(".size-btn");
    sizeButtons.forEach((button) => {
      button.addEventListener("click", function () {
        sizeButtons.forEach((b) => b.classList.remove("selected"));
        this.classList.add("selected");
      });
    });

    // Botón agregar al carrito
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
            if (!response.ok) throw new Error("Error HTTP: " + response.status);
            return response.json();
          })
          .then((data) => {
            if (data.success) {
              const cartCount = document.getElementById("cart-count");
              if (cartCount) {
                cartCount.textContent = data.total_items;
                cartCount.classList.remove("d-none");
              }

              // Modal o animación aquí si lo deseas
            } else {
              Swal.fire({ icon: "error", title: "Error", text: data.message });
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

// Función para obtener CSRF token
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
