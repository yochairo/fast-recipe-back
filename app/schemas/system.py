from pydantic import BaseModel, Field


class ApiInfoResponseDTO(BaseModel):
    title: str = Field(..., description="Nombre del proyecto / API")
    version: str = Field(..., description="Versión actual de la API")
    description: str = Field(..., description="Descripción del servicio")
    environment: str = Field(..., description="Entorno de ejecución actual")
    api_prefix: str = Field(..., description="Prefijo base de las rutas de la API")
    docs_url: str = Field(..., description="URL de documentación interactiva Swagger")
    redoc_url: str = Field(..., description="URL de documentación ReDoc")
    status: str = Field(default="ok", description="Estado operativo del servicio")


class HealthResponseDTO(BaseModel):
    status: str = Field(default="ok", description="Estado de salud del sistema")
    environment: str = Field(..., description="Entorno actual")
    version: str = Field(..., description="Versión de la API")

