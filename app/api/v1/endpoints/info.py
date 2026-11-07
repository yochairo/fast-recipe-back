from fastapi import APIRouter, status

from app.schemas.system import ApiInfoResponseDTO
from app.services.system_service import SystemService

router = APIRouter()


@router.get(
    "/info",
    response_model=ApiInfoResponseDTO,
    status_code=status.HTTP_200_OK,
    summary="Información general de la API",
    description="Retorna metadatos, versión y configuración de la API.",
)
def get_api_info() -> ApiInfoResponseDTO:
    return SystemService.get_api_info()

