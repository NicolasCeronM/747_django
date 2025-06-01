
# 🧢 SEVEN FOUR SEVEN — E-commerce de Moda Urbana con Impacto Social

Este proyecto es una tienda online desarrollada en Django orientada a la venta de productos de moda urbana. **SEVEN FOUR SEVEN** busca visibilizar talentos de sectores marginados, fusionando diseño independiente con innovación social.

## 🚀 Características principales

- ✅ Gestión de productos y categorías.
- 🎨 Sección de diseñadores destacados con páginas de perfil.
- 🛒 Carro de compras funcional.
- 💳 Integración con **Mercado Pago Checkout Pro**.
- 💳 Integración en desarrollo con **WebPay Plus**.
- 📦 Visualización y compra de drops (colecciones limitadas).
- 🎥 Soporte para videos promocionales en páginas de detalle.
- 🧩 Arquitectura modular basada en apps Django.

## 🏗️ Estructura del Proyecto

```bash
747_django/
├── apps/
│   ├── cart/               # Carrito de compras
│   ├── designer/           # Perfiles de diseñadores
│   ├── drop/               # Drops y productos
│   └── payments/           # Integración con pasarelas de pago
├── templates/              # Templates globales y base.html
├── static/                 # Archivos estáticos: CSS, JS, imágenes
├── media/                  # Archivos subidos como imágenes o videos
├── db.sqlite3              # Base de datos SQLite temporal
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno
└── manage.py               # Comando principal de Django
```

## 🛠️ Instalación y configuración

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/747_django.git
   cd 747_django
   ```

2. **Crea y activa un entorno virtual**
   ```bash
   python -m venv env
   source env/bin/activate  # o .\env\Scripts\activate en Windows
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno**

   Crea un archivo `.env` con las credenciales necesarias para Mercado Pago y Webpay (estos archivos se incluyen como referencia: `mp_credenciales.txt` y `webpay_credenciales.txt`).

5. **Aplica las migraciones y ejecuta el servidor**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 📷 Capturas de Pantalla (opcional)

> *(Agrega aquí imágenes de la tienda, páginas de detalle, carrito, etc.)*

## 📌 TODO y Roadmap

- [x] Implementación de carrito de compras.
- [x] Visualización de diseñadores y drops.
- [x] Integración con Mercado Pago.
- [ ] Integración con Webpay Plus.
- [ ] Sistema de registro e inicio de sesión para compradores.
- [ ] Dashboard para diseñadores y administración de drops.
- [ ] Pruebas unitarias con Pytest.
- [ ] Deployment en Render.com o similar.

## 🤝 Contribuciones

Este es un proyecto en constante evolución. Si deseas colaborar o tienes sugerencias, no dudes en abrir un issue o hacer un pull request.

## 📄 Licencia

Proyecto desarrollado con fines académicos y demostrativos. Derechos reservados © 2025 SEVEN FOUR SEVEN.

---

> **⚠️ Estado del Proyecto: En desarrollo 🛠️**
>
> Este repositorio está siendo activamente desarrollado. Algunas funcionalidades pueden no estar completas o en producción.
