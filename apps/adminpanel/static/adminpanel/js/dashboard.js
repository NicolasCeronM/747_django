document.addEventListener("DOMContentLoaded", function () {
  // Elementos del DOM
  const sidebar = document.getElementById("sidebar");
  const sidebarToggle = document.getElementById("sidebarToggle");
  const mobileMenuBtn = document.getElementById("mobileMenuBtn");
  const navLinks = document.querySelectorAll(".nav-link");
  const contentSections = document.querySelectorAll(".content-section");
  const pageTitle = document.getElementById("pageTitle");

  // Toggle sidebar (desktop)
  sidebarToggle.addEventListener("click", function () {
    sidebar.classList.toggle("collapsed");

    // Guardar estado en localStorage
    const isCollapsed = sidebar.classList.contains("collapsed");
    localStorage.setItem("sidebarCollapsed", isCollapsed);
  });

  // Toggle sidebar (mobile)
  mobileMenuBtn.addEventListener("click", function () {
    sidebar.classList.toggle("mobile-open");
  });

  // Cerrar sidebar en mobile al hacer clic fuera
  document.addEventListener("click", function (e) {
    if (window.innerWidth <= 1024) {
      if (!sidebar.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
        sidebar.classList.remove("mobile-open");
      }
    }
  });

  // Navegación entre secciones
  navLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();

      const targetSection = this.getAttribute("data-section");

      // Remover clase active de todos los links
      navLinks.forEach((l) => l.classList.remove("active"));

      // Agregar clase active al link clickeado
      this.classList.add("active");

      // Ocultar todas las secciones
      contentSections.forEach((section) => {
        section.classList.remove("active");
      });

      // Mostrar la sección target
      const targetElement = document.getElementById(targetSection);
      if (targetElement) {
        targetElement.classList.add("active");

        // Actualizar título de la página
        const sectionTitle = this.querySelector(".nav-text").textContent;
        pageTitle.textContent = sectionTitle;
      }

      // Cerrar sidebar en mobile después de navegar
      if (window.innerWidth <= 1024) {
        sidebar.classList.remove("mobile-open");
      }
    });
  });

  // Restaurar estado del sidebar desde localStorage
  const savedSidebarState = localStorage.getItem("sidebarCollapsed");
  if (savedSidebarState === "true") {
    sidebar.classList.add("collapsed");
  }

  // Simulación de datos en tiempo real
  function updateStats() {
    const statNumbers = document.querySelectorAll(".stat-number");

    statNumbers.forEach((stat) => {
      const currentValue = parseInt(stat.textContent.replace(/[^0-9]/g, ""));
      const change = Math.floor(Math.random() * 10) - 5; // Cambio aleatorio entre -5 y +5
      const newValue = Math.max(0, currentValue + change);

      // Formatear el número según el tipo
      if (stat.textContent.includes("$")) {
        stat.textContent = `$${newValue.toLocaleString()}`;
      } else {
        stat.textContent = newValue.toLocaleString();
      }
    });
  }

  // Actualizar estadísticas cada 30 segundos
  setInterval(updateStats, 30000);

  // Simulación de notificaciones
  function addNotification() {
    const notificationBadge = document.querySelector(".notification-badge");
    const currentCount = parseInt(notificationBadge.textContent);
    notificationBadge.textContent = currentCount + 1;

    // Animación de la notificación
    notificationBadge.style.animation = "pulse 0.5s ease-in-out";
    setTimeout(() => {
      notificationBadge.style.animation = "";
    }, 500);
  }

  // Agregar notificación cada 2 minutos
  setInterval(addNotification, 120000);

  // Funcionalidad de búsqueda
  const searchInput = document.querySelector(".search-input");
  const filterInput = document.querySelector(".filter-input");

  if (searchInput) {
    searchInput.addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase();
      console.log("Buscando:", searchTerm);
      // Aquí se implementaría la lógica de búsqueda real
    });
  }

  if (filterInput) {
    filterInput.addEventListener("input", function () {
      const filterTerm = this.value.toLowerCase();
      const tableRows = document.querySelectorAll(".data-table tbody tr");

      tableRows.forEach((row) => {
        const text = row.textContent.toLowerCase();
        if (text.includes(filterTerm)) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      });
    });
  }

  // Funcionalidad de paginación
  const paginationBtns = document.querySelectorAll(".pagination-btn");

  paginationBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      if (this.classList.contains("active")) return;

      // Remover active de todos los botones
      paginationBtns.forEach((b) => b.classList.remove("active"));

      // Agregar active al botón clickeado (si no es de navegación)
      if (!this.querySelector("i")) {
        this.classList.add("active");
      }

      console.log("Navegando a página:", this.textContent);
      // Aquí se implementaría la lógica de paginación real
    });
  });

  // Funcionalidad de acciones de tabla
  const actionBtns = document.querySelectorAll(".action-btn-small");

  actionBtns.forEach((btn) => {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();

      const icon = this.querySelector("i");
      const row = this.closest("tr");
      const userName = row.querySelector(".user-cell span").textContent;

      if (icon.classList.contains("fa-edit")) {
        console.log("Editando usuario:", userName);
        // Aquí se abriría un modal de edición
      } else if (icon.classList.contains("fa-trash")) {
        if (confirm(`¿Estás seguro de que quieres eliminar a ${userName}?`)) {
          console.log("Eliminando usuario:", userName);
          // Aquí se implementaría la lógica de eliminación
          row.style.animation = "fadeOut 0.3s ease-out";
          setTimeout(() => {
            row.remove();
          }, 300);
        }
      }
    });
  });

  // Funcionalidad de filtros
  const filterSelect = document.querySelector(".filter-select");

  if (filterSelect) {
    filterSelect.addEventListener("change", function () {
      const filterValue = this.value;
      const tableRows = document.querySelectorAll(".data-table tbody tr");

      tableRows.forEach((row) => {
        const statusBadge = row.querySelector(".status-badge");

        if (filterValue === "Todos los usuarios") {
          row.style.display = "";
        } else if (
          filterValue === "Activos" &&
          statusBadge.classList.contains("active")
        ) {
          row.style.display = "";
        } else if (
          filterValue === "Inactivos" &&
          statusBadge.classList.contains("inactive")
        ) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      });
    });
  }

  // Animaciones CSS adicionales
  const style = document.createElement("style");
  style.textContent = `
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        
        @keyframes fadeOut {
            from { opacity: 1; transform: translateX(0); }
            to { opacity: 0; transform: translateX(-20px); }
        }
        
        .nav-link {
            position: relative;
            overflow: hidden;
        }
        
        .nav-link::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.5s;
        }
        
        .nav-link:hover::after {
            left: 100%;
        }
        
        .stat-card {
            position: relative;
            overflow: hidden;
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 107, 0, 0.1), transparent);
            transition: left 0.6s;
        }
        
        .stat-card:hover::before {
            left: 100%;
        }
    `;
  document.head.appendChild(style);

  // Simulación de gráfico simple (reemplazar con Chart.js en producción)
  const canvas = document.getElementById("salesChart");
  if (canvas) {
    const ctx = canvas.getContext("2d");

    // Datos de ejemplo
    const data = [120, 190, 300, 500, 200, 300, 450];
    const labels = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];

    // Configuración del gráfico
    const chartWidth = canvas.width;
    const chartHeight = canvas.height;
    const padding = 40;
    const maxValue = Math.max(...data);

    // Limpiar canvas
    ctx.clearRect(0, 0, chartWidth, chartHeight);

    // Dibujar líneas de fondo
    ctx.strokeStyle = "#e9ecef";
    ctx.lineWidth = 1;

    for (let i = 0; i <= 5; i++) {
      const y = padding + (i * (chartHeight - 2 * padding)) / 5;
      ctx.beginPath();
      ctx.moveTo(padding, y);
      ctx.lineTo(chartWidth - padding, y);
      ctx.stroke();
    }

    // Dibujar línea de datos
    ctx.strokeStyle = "#ff6b00";
    ctx.lineWidth = 3;
    ctx.beginPath();

    data.forEach((value, index) => {
      const x =
        padding + (index * (chartWidth - 2 * padding)) / (data.length - 1);
      const y =
        chartHeight -
        padding -
        (value / maxValue) * (chartHeight - 2 * padding);

      if (index === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    });

    ctx.stroke();

    // Dibujar puntos
    ctx.fillStyle = "#ff6b00";
    data.forEach((value, index) => {
      const x =
        padding + (index * (chartWidth - 2 * padding)) / (data.length - 1);
      const y =
        chartHeight -
        padding -
        (value / maxValue) * (chartHeight - 2 * padding);

      ctx.beginPath();
      ctx.arc(x, y, 4, 0, 2 * Math.PI);
      ctx.fill();
    });

    // Dibujar etiquetas
    ctx.fillStyle = "#6c757d";
    ctx.font = "12px Inter";
    ctx.textAlign = "center";

    labels.forEach((label, index) => {
      const x =
        padding + (index * (chartWidth - 2 * padding)) / (data.length - 1);
      ctx.fillText(label, x, chartHeight - 10);
    });
  }

  // Manejo de responsive para sidebar
  function handleResize() {
    if (window.innerWidth > 1024) {
      sidebar.classList.remove("mobile-open");
    }
  }

  window.addEventListener("resize", handleResize);

  // Inicialización de tooltips (simulado)
  const tooltipElements = document.querySelectorAll("[data-tooltip]");

  tooltipElements.forEach((element) => {
    element.addEventListener("mouseenter", function () {
      const tooltipText = this.getAttribute("data-tooltip");
      console.log("Tooltip:", tooltipText);
      // Aquí se implementaría un sistema de tooltips real
    });
  });

  // Funcionalidad de logout
  const logoutBtn = document.querySelector(".logout-btn");

  if (logoutBtn) {
    logoutBtn.addEventListener("click", function () {
      if (confirm("¿Estás seguro de que quieres cerrar sesión?")) {
        console.log("Cerrando sesión...");
        // Aquí se implementaría la lógica de logout real
        // window.location.href = '/login';
      }
    });
  }

  // Funcionalidad de notificaciones
  const notificationBtn = document.querySelector(".notification-btn");

  if (notificationBtn) {
    notificationBtn.addEventListener("click", function () {
      console.log("Abriendo panel de notificaciones...");
      // Aquí se implementaría un panel de notificaciones
    });
  }

  console.log("Panel de administración inicializado correctamente");
});
