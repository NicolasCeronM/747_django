// ==========================
// Abrir modal de talento con loader
// ==========================
function openTalentModal(id) {
  const modal = document.getElementById("talentModal");
  const loader = document.getElementById("talentLoader");

  modal.style.display = "flex";
  loader.style.display = "flex"; // Mostrar loader

  fetch(`/adminpanel/talents/${id}/json/`)
    .then((res) => res.json())
    .then((data) => {
      // Info principal
      document.getElementById("talentAvatar").src = data.image_url;
      document.getElementById("talentName").innerText = data.full_name;
      document.getElementById(
        "talentBrand"
      ).innerText = `${data.brand_name} • ${data.specialty} - ${data.location}`;
      document.getElementById("talentVerified").style.display = data.is_verified
        ? "inline-block"
        : "none";

      // Info detallada
      document.getElementById("infoNombre").innerText = data.full_name;
      document.getElementById("infoMarca").innerText = data.brand_name;
      document.getElementById("infoEspecialidad").innerText = data.specialty;
      document.getElementById("infoUbicacion").innerText = data.location;
      document.getElementById("infoFecha").innerText = data.registered;
      document.getElementById("infoBio").innerText = data.biography;

      // Contacto
      document.getElementById("infoEmail").innerText = data.contact_email;
      document.getElementById(
        "infoEmail"
      ).href = `mailto:${data.contact_email}`;
      document.getElementById("infoTelefono").innerText = data.phone_number;
      document.getElementById("infoTelefono").href = `tel:${data.phone_number}`;

      // Video
      document.getElementById("talentVideo").src = data.video_url || "";

      // Redes sociales
      const redesHTML = data.social_links
        .map((link) => {
          let icon = "";
          switch (link.platform.toLowerCase()) {
            case "instagram":
              icon = "fab fa-instagram";
              break;
            case "facebook":
              icon = "fab fa-facebook-f";
              break;
            case "twitter":
              icon = "fab fa-twitter";
              break;
            case "youtube":
              icon = "fab fa-youtube";
              break;
            case "website":
              icon = "fas fa-globe";
              break;
            default:
              icon = "fas fa-link";
          }
          return `<a href="${link.url}" target="_blank"><i class="${icon}"></i></a>`;
        })
        .join("");

      document.getElementById("infoRedes").innerHTML = redesHTML;

      // Ocultar loader al terminar
      loader.style.display = "none";
    })
    .catch((err) => {
      loader.style.display = "none";
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudo cargar la información del talento.",
      });
    });
}

// ==========================
// Cerrar modal del talento
// ==========================
function closeTalentModal() {
  document.getElementById("talentModal").style.display = "none";
  document.getElementById("talentVideo").src = ""; // Detener video
}

// ==========================
// Confirmar eliminación
// ==========================
function confirmarEliminacion(talentId, talentName) {
  Swal.fire({
    title: "¿Eliminar talento?",
    text: `Esta acción eliminará a "${talentName}".`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#e11d48",
    cancelButtonColor: "#6b7280",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      // Crear formulario POST oculto
      const form = document.createElement("form");
      form.method = "POST";
      form.action = `/adminpanel/talento/${talentId}/eliminar/`;

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

// ==========================
// Mostrar mensaje de éxito de Django
// ==========================
document.addEventListener("DOMContentLoaded", function () {
  const mensaje = document.getElementById("swal-message");
  if (mensaje) {
    Swal.fire({
      icon: "success",
      title: "Éxito",
      text: mensaje.dataset.text,
      timer: 3000,
      showConfirmButton: false,
    });
  }
});
