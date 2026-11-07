from fastapi import APIRouter, status

from app.schemas.system import HealthResponseDTO
from app.services.system_service import SystemService

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponseDTO,
    status_code=status.HTTP_200_OK,
    summary="Verificación de estado del servicio",
    description="Retorna el estado de salud y operatividad básico del backend.",
)
def check_health() -> HealthResponseDTO:
    return SystemService.get_health()

