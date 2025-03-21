
<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, alto rendimiento, fácil de aprender, rápido de codificar, listo para producción</em>
</p>
<p align="center">
<a href="https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**Source Code**: <a href="https://github.com/fastapi/fastapi" target="_blank">https://github.com/fastapi/fastapi</a>

---



## UserHub
Api para gestionar usuarios, desarrollada con **FastAPI** y **MongoDB**. Ofrece operaciones CRUD, paginación, filtros y validaciones de datos. Diseñada para ser rápida, segura y fácil de usar.

### Características Principales
- **CRUD de Usuarios**: Crear, leer, actualizar y eliminar usuarios.
- **Paginación y Filtros**: Listar usuarios con paginación y filtros.
- **Validaciones**: Validación de datos utilizando Pydantic.
- **Docker**: Fácil despliegue con Docker y Docker Compose.
- **Swagger UI**: Documentación interactiva de la API.

### Requisitos Previos
Antes de instalar y ejecutar la API, asegúrate de tener instaladas las siguientes herramientas:

- **Docker:** Para ejecutar la aplicación en un contenedor.
    - <a href="https://docs.docker.com/get-started/get-docker/" target="_blank">Guía de instalación</a>
- **Docker Compose:** Para gestionar múltiples contenedores (opcional, pero recomendado).
    - <a href="https://docs.docker.com/compose/install/" target="_blank">Instalar Docker Compose</a>
- **Python (opcional):**
    - <a href="https://www.python.org/downloads/" target="_blank">Descargar Python</a>
    - Versión recomendada: Python 3.9 o superior.
- **Git (opcional):** Para clonar el repositorio.
  - <a href="https://git-scm.com/" target="_blank">Descargar Git</a>

### Instalación
Sigue estos pasos para configurar y ejecutar la API:

1. Clonar el Repositorio
Si tienes Git instalado, clona el repositorio:

```bash
git clone https://github.com/olivaresoliver13/api-user-hub.git
cd tu-repositorio
```
Si no tienes Git, descarga el repositorio como un archivo ZIP y descomprímelo.

2. Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto con las siguientes variables:

```env
PYTHONPATH=/app
MONGO_URI=mongodb://mongo:27017
MONGO_DB=users
```

3. Ejecutar con Docker Compose
Construye y levanta los contenedores con Docker Compose:

```bash
docker-compose up --build
```
Esto hará lo siguiente:
- Construirá la imagen de Docker para la API.
- Levantará un contenedor para la API y otro para MongoDB.
- Expondrá la API en http://localhost:8080.

4. Acceder a la API
Una vez que los contenedores estén en ejecución, puedes acceder a la API en:
- API: http://localhost:8080
- Swagger UI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc

5. Ejecución Local (Opcional)
Si prefieres ejecutar la API sin Docker:

- Instala las dependencias:

```bash
pip install -r requirements.txt
```

- Ejecuta la aplicación:

```bash
uvicorn app.main:app --reload
``` 
Accede a la API en http://localhost:8080.


6. Pruebas
Para ejecutar las pruebas:

- Instala las dependencias de desarrollo:

```bash
pip install -r requirements-dev.txt
```

- Ejecuta las pruebas:

```bash
pytest
```

8. Detener los Contenedores
Para detener los contenedores, ejecuta:

```bash
docker-compose down
```

### Documentación
 <a href="http://0.0.0.0:8080/docs" target="_blank">Swagger UI</a>

### Estructura del Proyecto
```txt
api-user-hub/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── crud/
│   ├── api/
│   └── db/
├── tests/
│   ├── __init__.py
│   └── test_users.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

### Contribución
¡Gracias por tu interés en contribuir a este proyecto! Tu ayuda es muy valiosa. A continuación, te explicamos cómo puedes contribuir:

1. Haz un Fork del Repositorio
- Haz un fork del repositorio en GitHub.

- Clona tu fork localmente:

```bash
git clone https://github.com/olivaresoliver13/api-user-hub
cd tu-repositorio
```
2. Configura tu Entorno de Desarrollo
- Asegúrate de tener instaladas las herramientas necesarias:

    - Docker
    - Docker Compose
    - Python 3.9+ (opcional, para desarrollo local).
    - Crea un archivo .env en la raíz del proyecto con las siguientes variables:

    ```env
    PYTHONPATH=/app
    MONGO_URI=mongodb://mongo:27017
    MONGO_DB=users
    ```

- Levanta los contenedores con Docker Compose:

```bash
docker-compose up --build
```

- Accede a la API en http://localhost:8080.

3. Crea una Rama para tu Contribución
Crea una rama para tu feature o corrección:

```bash
git checkout -b feature/nueva-funcionalidad
```
- Usa un nombre descriptivo para la rama, como:

    - feature/agregar-paginacion
    - fix/corregir-error-autenticacion

4. Realiza tus Cambios
- Desarrolla tu feature o corrección.
- Asegúrate de seguir las mejores prácticas de código:

    - Usa nombres descriptivos para variables y funciones.
    - Mantén el código limpio y bien documentado.
    - Escribe pruebas unitarias para nuevas funcionalidades.
- Ejecuta las pruebas para asegurarte de que todo funciona correctamente:

```bash
pytest
```

5. Haz Commit de tus Cambios
Agrega tus cambios al área de staging:


```bash
git add .
```

- Haz commit de tus cambios con un mensaje descriptivo:

```bash
git commit -m "Agregar paginación a la lista de usuarios"
```
Usa el formato Conventional Commits para los mensajes de commit:

- feat: Para nuevas funcionalidades.
- fix: Para correcciones de errores.
- docs: Para cambios en la documentación.
- test: Para agregar o modificar pruebas.
- chore: Para tareas de mantenimiento.

6. Haz Push a tu Rama
- Sube tus cambios a tu fork en GitHub:

```bash
git push origin feature/nueva-funcionalidad
```

7. Abre un Pull Request (PR)
- Ve a la página del repositorio original en GitHub.
- Haz clic en New Pull Request.
- Selecciona tu rama y describe los cambios realizados.
- Asegúrate de que:

    - título del PR sea claro y descriptivo.
    - La descripción incluya los detalles de los cambios.
    - Todas las pruebas hayan pasado.

8. Revisión y Aprobación
- Espera a que los mantenedores revisen tu PR.
- Realiza los cambios solicitados si es necesario.
- Una vez aprobado, tu contribución será fusionada con la rama principal.

9. Agradecimientos
¡Gracias por contribuir! Tu esfuerzo ayuda a mejorar este proyecto para todos. 🚀

---