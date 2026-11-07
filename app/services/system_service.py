from app.core.config import settings
from app.schemas.system import ApiInfoResponseDTO, HealthResponseDTO


class SystemService:
    @staticmethod
    def get_api_info() -> ApiInfoResponseDTO:
        return ApiInfoResponseDTO(
            title=settings.PROJECT_NAME,
            version=settings.VERSION,
            description="API RESTful para la gestión y recomendación de recetas rápidas (Fast Recipe).",
            environment=settings.ENVIRONMENT,
            api_prefix=settings.API_V1_STR,
            docs_url="/docs",
            redoc_url="/redoc",
            status="ok",
        )

    @staticmethod
    def get_health() -> HealthResponseDTO:
        return HealthResponseDTO(
            status="ok",
            environment=settings.ENVIRONMENT,
            version=settings.VERSION,
        )

