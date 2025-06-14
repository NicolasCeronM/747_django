function setCookie(name, value, days) {
  const expires = new Date(Date.now() + days * 864e5).toUTCString();
  document.cookie =
    name +
    "=" +
    encodeURIComponent(value) +
    "; expires=" +
    expires +
    "; path=/";
}

function getCookie(name) {
  return document.cookie.split("; ").reduce((r, v) => {
    const parts = v.split("=");
    return parts[0] === name ? decodeURIComponent(parts[1]) : r;
  }, "");
}

function showPopup() {
  document.getElementById("popup").style.display = "flex";
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
}

function acceptPopup() {
  const email = document.getElementById("popupEmail").value;
  if (!email || !email.includes("@")) {
    alert("Por favor ingresa un correo válido.");
    return;
  }

  console.log("Correo capturado:", email); // Aquí podrías enviar el correo al backend
  setCookie("popup_drops_custom", "aceptado", 7);
  closePopup();
  alert("¡Gracias! Te avisaremos antes que nadie.");
}

function rejectPopup() {
  setCookie("popup_drops_custom", "rechazado", 7);
  closePopup();
}

document.addEventListener("DOMContentLoaded", function () {
  if (!getCookie("popup_drops_custom")) {
    showPopup();
  }
});

function acceptPopup() {
  const email = document.getElementById("popupEmail").value.trim();
  const consent = document.getElementById("popupConsent").checked;
  const errorDiv = document.getElementById("popupError");

  // Resetear mensaje de error
  errorDiv.style.display = "none";
  errorDiv.innerText = "";

  // Validar correo
  if (!email || !email.includes("@") || !email.includes(".")) {
    errorDiv.innerText = "Por favor ingresa un correo válido.";
    errorDiv.style.display = "block";
    return;
  }

  // Validar checkbox
  if (!consent) {
    errorDiv.innerText = "Debes aceptar recibir comunicaciones por email.";
    errorDiv.style.display = "block";
    return;
  }

  // TODO: Enviar al backend si deseas con fetch()

  // Éxito
  setCookie("popup_drops_custom", "aceptado", 7);
  document.getElementById("subscriptionForm").style.display = "none";
  document.getElementById("successState").style.display = "flex";
}
