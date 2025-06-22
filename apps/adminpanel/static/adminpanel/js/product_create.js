document.addEventListener("DOMContentLoaded", () => {
  // === TALLAS (chips dinámicos) ===
  const input = document.getElementById("size-input");
  const list = document.getElementById("size-tags");

  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === ",") {
      e.preventDefault();
      const value = input.value.trim().toUpperCase();
      if (value !== "" && !tagExists(value)) {
        addTag(value);
        input.value = "";
      }
    }
  });

  function tagExists(val) {
    return [...document.querySelectorAll("input[name='sizes']")].some(
      (i) => i.value === val
    );
  }

  function addTag(text) {
    const li = document.createElement("li");
    li.className = "tag";

    const span = document.createElement("span");
    span.textContent = text;

    const remove = document.createElement("button");
    remove.className = "remove-tag";
    remove.textContent = "✕";
    remove.onclick = () => li.remove();

    const hidden = document.createElement("input");
    hidden.type = "hidden";
    hidden.name = "sizes";
    hidden.value = text;

    li.appendChild(span);
    li.appendChild(remove);
    li.appendChild(hidden);
    list.appendChild(li);
  }

  // === Previsualización de imágenes ===
  const imageInput = document.getElementById("images-main");
  const previewContainer = document.getElementById("image-preview");

  imageInput.addEventListener("change", () => {
    previewContainer.innerHTML = "";
    [...imageInput.files].forEach((file) => {
      const reader = new FileReader();
      reader.onload = (e) => {
        const img = document.createElement("img");
        img.src = e.target.result;
        previewContainer.appendChild(img);
      };
      reader.readAsDataURL(file);
    });
  });
});

// === Añadir dinámicamente campos de imagen ===
document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("image-input");
  const previewContainer = document.getElementById("preview-container");
  const uploadedFiles = [];

  input.addEventListener("change", function () {
    const newFiles = Array.from(this.files);

    newFiles.forEach((file) => {
      if (file && file.type.startsWith("image/")) {
        uploadedFiles.push(file);

        const reader = new FileReader();
        reader.onload = function (e) {
          const img = document.createElement("img");
          img.src = e.target.result;
          img.className = "image-thumb";
          img.style.maxHeight = "120px";
          img.style.margin = "5px";
          img.style.borderRadius = "8px";
          previewContainer.appendChild(img);
        };
        reader.readAsDataURL(file);
      }
    });

    // Actualizar el input con todos los archivos acumulados
    const dataTransfer = new DataTransfer();
    uploadedFiles.forEach((f) => dataTransfer.items.add(f));
    input.files = dataTransfer.files;
  });
});
