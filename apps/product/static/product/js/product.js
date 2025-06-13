document.addEventListener("DOMContentLoaded", function () {
  // Funcionalidad para cambiar imágenes al pasar el mouse por las cards
  const productCards = document.querySelectorAll(".product-card");

  productCards.forEach((card) => {
    const images = card.querySelectorAll(".product-images img");
    const indicators = card.querySelectorAll(".image-indicators .indicator");
    let currentIndex = 0;
    let interval;

    // Iniciar rotación de imágenes al pasar el mouse
    card.addEventListener("mouseenter", () => {
      if (images.length <= 1) return;

      interval = setInterval(() => {
        // Quitar clase activa de la imagen e indicador actual
        images[currentIndex].classList.remove("active");
        indicators[currentIndex].classList.remove("active");

        // Actualizar índice
        currentIndex = (currentIndex + 1) % images.length;

        // Añadir clase activa a la nueva imagen e indicador
        images[currentIndex].classList.add("active");
        indicators[currentIndex].classList.add("active");
      }, 1000); // Cambiar imagen cada segundo
    });

    // Detener rotación al quitar el mouse
    card.addEventListener("mouseleave", () => {
      clearInterval(interval);

      // Restaurar la primera imagen
      images.forEach((img, index) => {
        img.classList.toggle("active", index === 0);
      });

      // Restaurar el primer indicador
      indicators.forEach((indicator, index) => {
        indicator.classList.toggle("active", index === 0);
      });

      currentIndex = 0;
    });

    // Permitir clic en los indicadores para cambiar la imagen
    indicators.forEach((indicator, index) => {
      indicator.addEventListener("click", (e) => {
        e.stopPropagation(); // Evitar que el evento se propague

        // Detener el intervalo si está activo
        clearInterval(interval);

        // Quitar clase activa de todas las imágenes e indicadores
        images.forEach((img) => img.classList.remove("active"));
        indicators.forEach((ind) => ind.classList.remove("active"));

        // Activar la imagen e indicador seleccionados
        images[index].classList.add("active");
        indicator.classList.add("active");

        // Actualizar el índice actual
        currentIndex = index;
      });
    });
  });

  // Funcionalidad para los botones de talla
  const sizeButtons = document.querySelectorAll(".size-btn");

  sizeButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Quitar selección de otros botones en el mismo grupo
      const siblings = this.parentElement.querySelectorAll(".size-btn");
      siblings.forEach((sibling) => {
        sibling.classList.remove("selected");
      });

      // Seleccionar este botón
      this.classList.add("selected");
    });
  });

  // Funcionalidad para el botón de agregar al carrito
  const addToCartButtons = document.querySelectorAll(".add-to-cart");

  addToCartButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const productCard = this.closest(".product-card");
      const productName =
        productCard.querySelector(".product-name").textContent;

      // Animación de botón
      const originalText = this.textContent;
      this.textContent = "✓ Agregado";

      setTimeout(() => {
        this.textContent = originalText;
      }, 1500);

      // Aquí se podría implementar la lógica real para agregar al carrito
      console.log(`Producto agregado: ${productName}`);
    });
  });

  // Funcionalidad para el filtro
  const aplicarBtn = document.getElementById("aplicar");
  const limpiarBtn = document.getElementById("limpiar");
  const categoriaSelect = document.getElementById("categoria");
  const searchInput = document.getElementById("search");

  aplicarBtn.addEventListener("click", function () {
    const categoria = categoriaSelect.value;
    const searchTerm = searchInput.value.toLowerCase();

    productCards.forEach((card) => {
      const productName = card
        .querySelector(".product-name")
        .textContent.toLowerCase();
      const productBrand = card
        .querySelector(".product-brand")
        .textContent.toLowerCase();

      let showCard = true;

      // Filtrar por categoría
      if (categoria && !productName.includes(categoria.toLowerCase())) {
        showCard = false;
      }

      // Filtrar por término de búsqueda
      if (
        searchTerm &&
        !productName.includes(searchTerm) &&
        !productBrand.includes(searchTerm)
      ) {
        showCard = false;
      }

      card.style.display = showCard ? "block" : "none";
    });
  });

  limpiarBtn.addEventListener("click", function () {
    categoriaSelect.value = "";
    searchInput.value = "";

    productCards.forEach((card) => {
      card.style.display = "block";
    });
  });

  // Funcionalidad para la paginación
  const pageButtons = document.querySelectorAll(".page-btn");

  pageButtons.forEach((button) => {
    button.addEventListener("click", function () {
      if (this.classList.contains("next")) return;

      pageButtons.forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");
    });
  });
});
