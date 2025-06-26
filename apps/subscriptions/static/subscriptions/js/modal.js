document.addEventListener("DOMContentLoaded", function () {
  const popup = document.getElementById("popup");
  const errorBox = document.getElementById("popupError");
  const emailInput = document.getElementById("popupEmail");
  const consentCheckbox = document.getElementById("popupConsent");
  const successState = document.getElementById("successState");
  const formState = document.getElementById("subscriptionForm");

  function daysBetween(d1, d2) {
    const diffTime = Math.abs(d2 - d1);
    return diffTime / (1000 * 60 * 60 * 24);
  }

  function shouldShowPopup() {
    const subscribed = localStorage.getItem("modalSubscribed");
    const closedAt = localStorage.getItem("modalClosedAt");
    const shownThisSession = sessionStorage.getItem("modalShownThisSession");

    if (subscribed === "true") return false;
    if (shownThisSession === "true") return false;

    if (closedAt) {
      const closedDate = new Date(parseInt(closedAt));
      const now = new Date();
      const days = daysBetween(closedDate, now);
      return days >= 3;
    }

    return true;
  }

  if (shouldShowPopup()) {
    setTimeout(() => {
      popup.style.display = "flex";
      sessionStorage.setItem("modalShownThisSession", "true");
    }, 1000);
  }

  window.rejectPopup = function () {
    popup.style.display = "none";
    localStorage.setItem("modalClosedAt", Date.now().toString());
  };

  window.closePopup = function () {
    popup.style.display = "none";
  };

  window.acceptPopup = function () {
    const email = emailInput.value.trim();
    const accepted = consentCheckbox.checked;

    if (!accepted) {
      errorBox.style.display = "block";
      errorBox.innerText = "Debes aceptar recibir comunicaciones.";
      return;
    }

    if (!email || !email.includes("@")) {
      errorBox.style.display = "block";
      errorBox.innerText = "Correo inválido.";
      return;
    }

    fetch("/suscripciones/registrar/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({ email: email, accepted: accepted }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          localStorage.setItem("modalSubscribed", "true");
          formState.style.display = "none";
          successState.style.display = "flex";
        } else {
          errorBox.style.display = "block";
          errorBox.innerText = data.error || "Error al suscribirse.";
        }
      })
      .catch(() => {
        errorBox.style.display = "block";
        errorBox.innerText = "Error de red.";
      });
  };

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
