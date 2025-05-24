document.addEventListener("DOMContentLoaded", function () {
  const video = document.getElementById("previewVideo");

  if (video) {
    video.addEventListener("click", () => {
      video.pause(); // detener el loop silenciado
      video.muted = false; // activar sonido
      video.controls = true; // mostrar controles
      video.loop = false; // dejar que termine si quiere

      // abrir en pantalla completa
      if (video.requestFullscreen) {
        video.requestFullscreen();
      } else if (video.webkitRequestFullscreen) {
        video.webkitRequestFullscreen();
      } else if (video.msRequestFullscreen) {
        video.msRequestFullscreen();
      }

      video.play(); // volver a reproducir con sonido
    });
  }
});
