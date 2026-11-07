AGENTS.md - Contexto y Reglas para Agentes de IA

Este documento define la arquitectura, normas de diseño y comandos del proyecto fast_recipe_back. Consúltalo para mantener consistencia y eficiencia.

🛠️ Tech Stack Base

Lenguaje: Python 3.10+ (Con Type Hints explícitos obligatorios).

Framework: FastAPI (REST API).

Gestor de Paquetes: Poetry (python -m poetry).

Validación / DTOs: Pydantic v2 (pydantic-settings para entorno).

ORM / Persistencia: SQLAlchemy / SQLModel.

🏗️ Arquitectura y Capas (Separación Estricta)

app/schemas/ (DTOs):

Define ÚNICAMENTE modelos Pydantic (Request y Response).

Prohibido incluir lógica de base de datos o servicios aquí.

Nombres claros: UserCreateDTO, UserResponseDTO, RecipeUpdateDTO.

app/services/ (Lógica de Negocio):

Contiene la regla de negocio pura.

Recibe DTOs o tipos primitivos, procesa y retorna modelos ORM o DTOs.

Recibe la sesión de la base de datos (db: Session) por inyección/parámetro.

No maneja solicitudes HTTP (Request/Response) directamente.

app/api/ (Controladores / Endpoints):

Recibe solicitudes HTTP.

Valida la entrada mediante schemas.

Llama a la capa de services correspondiente.

Lanza excepciones HTTP (HTTPException) según el resultado de la capa de servicios.

PROHIBIDO: Realizar consultas SQL o lógica de negocio compleja en esta capa.

app/models/ (Persistencia):

Define únicamente los modelos ORM de la base de datos.

app/core/ (Configuración y Utilidades Globales):

Contiene config.py (BaseSettings), conexión a DB y utilidades de seguridad (hashing, JWT).

🛑 Reglas Estrictas para la IA (Guardrails)

Cero Leaks de ORM: NUNCA retornes un objeto Model (ORM) directamente desde un endpoint si este expone datos sensibles. Usa un DTO (schema) en el response_model.

Inyección de Dependencias: Usa Depends(get_db) en los endpoints de api/ para pasar la sesión a los servicios.

Formato de Archivos: No crees scripts sueltos fuera de la estructura definida en app/.

Manejo de Paquetes: No sugieras pip install. Usa siempre python -m poetry add <package>.

💻 Comandos Frecuentes

# Levantar servidor de desarrollo
python -m poetry run uvicorn app.main:app --reload

# Agregar dependencia de producción
python -m poetry add <nombre-paquete>

# Agregar dependencia de desarrollo
python -m poetry add <nombre-paquete> --group dev
