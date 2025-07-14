<<<<<<< HEAD
# Sistema de Inventario Django

Aplicación web para gestionar productos en stock, con funcionalidades CRUD, autenticación de usuarios y control de historial de cambios.

## Características principales

- CRUD completo de productos
- Gestión de proveedores
- Sistema de autenticación (registro e inicio de sesión)
- Historial de cambios en el stock
- Búsqueda y filtrado de productos
- Interfaz responsive con Bootstrap

## Tecnologías utilizadas

- Python 3.x
- Django 4.x
- Bootstrap 5
- SQLite (base de datos por defecto)

## Instalación local

1. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

2. Instalar dependencias:

```bash
pip install django
```

3. Crear proyecto y aplicación:

```bash
django-admin startproject sistema_inventario .
python manage.py startapp inventario
```

4. Configurar settings.py (agregar apps y LOGIN_URL)

5. Realizar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crear superusuario:

```bash
python manage.py createsuperuser
```

7. Ejecutar servidor:

```bash
python manage.py runserver
```

8. Acceder en el navegador:

http://localhost:8000

## Pasos adicionales para completar el proyecto:

- Implementar modelos, vistas, formularios, URLs y plantillas según especificación.
- Añadir validaciones, paginación y mejoras de diseño.
- Configurar despliegue en producción.

Licencia MIT
=======
# InventorySystem
>>>>>>> fe079c64ae1315efe997ec4a4896ecce6fadd9c5
