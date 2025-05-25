// Referencias a elementos del DOM
const form = document.getElementById("loginForm");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");
const loginButton = document.getElementById("loginButton");
const loadingSpinner = document.getElementById("loadingSpinner");
const buttonText = document.getElementById("buttonText");
const successMessage = document.getElementById("successMessage");

// Toggle para mostrar/ocultar contraseña
togglePassword.addEventListener("click", function () {
  const type =
    passwordInput.getAttribute("type") === "password" ? "text" : "password";
  passwordInput.setAttribute("type", type);
  this.textContent = type === "password" ? "👁️" : "🙈";
});

// Validación en tiempo real
usernameInput.addEventListener("input", function () {
  validateField(this, "username");
});

passwordInput.addEventListener("input", function () {
  validateField(this, "password");
});

// Función de validación
function validateField(field, type) {
  const value = field.value.trim();
  const errorElement = document.getElementById(type + "Error");

  field.classList.remove("error", "success");
  errorElement.classList.remove("show");

  if (type === "username") {
    if (value.length === 0) {
      showError(field, errorElement, "El nombre de usuario es requerido");
      return false;
    } else if (value.length < 3) {
      showError(
        field,
        errorElement,
        "El nombre de usuario debe tener al menos 3 caracteres"
      );
      return false;
    } else {
      showSuccess(field);
      return true;
    }
  }

  if (type === "password") {
    if (value.length === 0) {
      showError(field, errorElement, "La contraseña es requerida");
      return false;
    } else if (value.length < 6) {
      showError(
        field,
        errorElement,
        "La contraseña debe tener al menos 6 caracteres"
      );
      return false;
    } else {
      showSuccess(field);
      return true;
    }
  }
}

function showError(field, errorElement, message) {
  field.classList.add("error");
  errorElement.textContent = message;
  errorElement.classList.add("show");
}

function showSuccess(field) {
  field.classList.add("success");
}

// Manejo del envío del formulario
form.addEventListener("submit", function (e) {
  e.preventDefault();

  const isUsernameValid = validateField(usernameInput, "username");
  const isPasswordValid = validateField(passwordInput, "password");

  if (isUsernameValid && isPasswordValid) {
    // Simular proceso de login
    loginButton.disabled = true;
    loadingSpinner.style.display = "inline-block";
    buttonText.textContent = "Iniciando sesión...";

    // Simular llamada a API
    setTimeout(() => {
      // Simular login exitoso
      form.style.display = "none";
      successMessage.style.display = "block";

      // Simular redirección
      setTimeout(() => {
        alert(
          "¡Login exitoso! En una aplicación real, serías redirigido al dashboard."
        );
        // Resetear formulario para demo
        form.style.display = "block";
        successMessage.style.display = "none";
        form.reset();
        loginButton.disabled = false;
        loadingSpinner.style.display = "none";
        buttonText.textContent = "Entrar";
        usernameInput.classList.remove("success");
        passwordInput.classList.remove("success");
      }, 2000);
    }, 1500);
  }
});

// Efecto de enfoque automático
window.addEventListener("load", function () {
  usernameInput.focus();
});
