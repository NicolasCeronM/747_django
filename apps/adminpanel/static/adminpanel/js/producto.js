document.addEventListener("DOMContentLoaded", function () {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 300);
    }, 4000);
  });
});

function confirmarEliminacion(productId, productName) {
  Swal.fire({
    title: "¿Eliminar producto?",
    text: `Esta acción eliminará: "${productName}"`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#e11d48",
    cancelButtonColor: "#6b7280",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      // Crear formulario y enviarlo
      const form = document.createElement("form");
      form.method = "POST";
      form.action = `/adminpanel/producto/${productId}/eliminar/`;

      const csrfToken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      const csrfInput = document.createElement("input");
      csrfInput.type = "hidden";
      csrfInput.name = "csrfmiddlewaretoken";
      csrfInput.value = csrfToken;

      form.appendChild(csrfInput);
      document.body.appendChild(form);
      form.submit();
    }
  });
}
