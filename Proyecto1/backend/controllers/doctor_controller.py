from fastapi import APIRouter, Body
from services.doctor_service import DoctorService

def doctor_router(service: DoctorService) -> APIRouter:
    router = APIRouter(prefix="/doctor", tags=["doctor"])

    @router.get("/health", summary="Verificar el estado de la API")
    def get_health():
        return {"status": "healthy"}

    @router.get("/sintomas", summary="Obtener todos los síntomas")
    def get_sintomas():
        return service.get_sintomas()
    


    return router