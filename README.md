# Fast Recipe Backend (`fast_recipe_back`)

API RESTful desarrollada con **FastAPI** y **Python**, administrada mediante **Poetry** para garantizar un entorno virtual aislado y reproducible. El proyecto está estructurado siguiendo una arquitectura por capas desacoplada (DTOs, Servicios, Modelos y Controladores).

---

## 🏗️ Arquitectura del Proyecto

El código fuente sigue una separación clara de responsabilidades dentro del directorio `app/`:

```text
fast_recipe_back/
├── app/
│   ├── api/                  # Capa HTTP (Controladores / Routers)
│   │   ├── v1/
│   │   │   ├── endpoints/    # Endpoints específicos por recurso (ej. health.py, auth.py)
│   │   │   └── api.py        # Agregador general de rutas v1
│   │   └── deps.py           # Inyección de dependencias (Sesiones DB, Seguridad, etc.)
│   ├── core/                 # Configuración global del sistema
│   │   ├── config.py         # Carga de variables de entorno (Pydantic BaseSettings)
│   │   ├── database.py       # Configuración y conexión a Base de Datos
│   │   └── security.py       # Funciones de hashing, JWT y encriptación
│   ├── models/               # Modelos de Base de Datos (Mapeo ORM: SQLAlchemy / SQLModel)
│   ├── schemas/              # DTOs (Pydantic Models para Request Body y Response)
│   ├── services/             # Lógica de Negocio pura (Reglas de negocio y casos de uso)
│   └── main.py               # Punto de entrada de la aplicación FastAPI
├── .env                      # Variables de entorno locales (No subir al control de versiones)
├── .gitignore                # Archivos excluidos de Git
├── pyproject.toml            # Definición de dependencias y metadata del proyecto
├── poetry.lock               # Bloqueo de versiones exactas instaladas
└── README.md                 # Documentación del proyecto
```

---

## 🧩 Flujo de Trabajo entre Capas

1. **`schemas/` (DTOs):** Validan el cuerpo de las peticiones de entrada (*Request Body*) y moldean la estructura del JSON de salida (*Response Body*).
2. **`api/` (Endpoints):** Reciben la solicitud HTTP, validan los datos utilizando los DTOs y delegan la ejecución a la capa de servicio.
3. **`services/` (Lógica de Negocio):** Contienen las reglas de negocio aisladas de la infraestructura web o del framework.
4. **`models/` (Persistencia):** Representan las entidades de la base de datos y gestionan las operaciones de persistencia.

---

## 🚀 Requisitos Previos

* **Python 3.10+**
* **Poetry** (gestor de dependencias)

---

## 🛠️ Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd fast_recipe_back
   ```

2. **Instalar dependencias del proyecto:**
   ```bash
   python -m poetry install
   ```

3. **Configurar variables de entorno:**
   Copia el archivo `.env.example` a `.env` en la raíz del proyecto y ajusta las variables según sea necesario:
   ```env
   PROJECT_NAME="Fast Recipe Backend"
   API_V1_STR="/api/v1"
   ```

---

## ⚡ Ejecución en Desarrollo

Para levantar el servidor de desarrollo local con recarga automática (*live reload*):

```bash
python -m poetry run uvicorn app.main:app --reload
```

El servidor estará disponible en: `http://127.0.0.1:8000`

---

## 📚 Documentación Interactiva (OpenAPI / Swagger)

FastAPI genera automáticamente la documentación interactiva de la API:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`
* **Health Check Endpoint:** `http://127.0.0.1:8000/api/v1/health`

---

## 📦 Gestión de Librerías

Para añadir nuevas dependencias al proyecto manteniendo el archivo `poetry.lock` actualizado:

* **Agregar librería de producción:**
  ```bash
  python -m poetry add nombre-libreria
  ```

* **Agregar librería de desarrollo:**
  ```bash
  python -m poetry add nombre-libreria --group dev
  ```