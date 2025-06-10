$(document).ready(function () {
  $(".add-to-cart-btn").on("click", function () {
    const productId = $(this).data("product-id");

    $.ajax({
      url: "/cart/add/",
      method: "POST",
      data: {
        product_id: productId,
        quantity: 1,
        csrfmiddlewaretoken: getCSRFToken(),
      },
      dataType: "json",
      success: function (data) {
        // console.log("Respuesta:", data);

        if (data.success) {
          $("#cart-count").text(data.cart_count);

          Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Producto agregado al carrito",
            showConfirmButton: false,
            timer: 1500,
          });
        } else {
          Swal.fire({
            icon: "error",
            title: "Error",
            text: "No se pudo agregar el producto.",
          });
        }
      },
      error: function (xhr, status, error) {
        console.error("Error en AJAX:", xhr.responseText);
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Ocurrió un problema al agregar el producto.",
        });
      },
    });
  });

  function getCSRFToken() {
    return $("input[name=csrfmiddlewaretoken]").val() || getCookie("csrftoken");
  }

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
});
