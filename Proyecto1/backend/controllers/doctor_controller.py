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
    
    @router.post("/obtener_falla", summary="Obtener fallas por lista de sintomas")
    def get_fallas(data: dict = Body(...)):
        print(f"Datos recibidos para obtener falla: {data}")
        listaSintomas = data.get("sintomas")
        if not listaSintomas:
            return {
                "success": False,
                "message": "El campo 'sintomas' es requerido.",
                "code": 400
            }
        return service.get_falla(listaSintomas)

    @router.get("/recomendaciones", summary="Obtener recomendaciones por falla")
    def get_recomendaciones_by_falla(fail:str):
        if not fail:
            return {
                "success": False,
                "message": "El campo 'fail' es requerido.",
                "code": 400
            }
        return service.get_recomendaciones_by_falla(fail)
    
    @router.post("/recomendaciones", summary="Obtener recomendaciones por sintomas")
    def get_recomendaciones_by_sintomas(data: dict = Body(...)):
        listaSintomas = data.get("sintomas")
        listaSintomas = data.get("sintomas")
        if not listaSintomas:
            return {
                "success": False,
                "message": "El campo 'sintomas' es requerido.",
                "code": 400
            }
        return service.get_recomendaciones_by_sintomas(listaSintomas)

    @router.post("/sintoma", summary="Agregar un nuevo síntoma")
    def add_sintoma(data: dict = Body(...)):
        sintoma = data.get("sintoma")
        if not sintoma:
            return {
                "success": False,
                "message": "El campo 'sintoma' es requerido.",
                "code": 400
            }
        return service.add_sintoma(sintoma)

    @router.post("/falla", summary="Crear/guardar falla")
    def add_falla(data: dict = Body(...)):
        falla = data.get("falla")
        if not falla:
            return {
                "success": False,
                "message": "El campo 'falla' es requerido.",
                "code": 400
            }
        return service.add_falla(falla)

    @router.post("/recomendacion", summary="Agregar nueva recomendacion")
    def add_recomendacion(data: dict = Body(...)):
        recomendacion = data.get("recomendacion")
        if not recomendacion:
            return {
                "success": False,
                "message": "El campo 'recomendacion' es requerido.",
                "code": 400
            }
        return service.add_recomendacion(recomendacion)
    
    @router.post("/falla_sintoma", summary="Adjudicar sintoma a falla")
    def conectar_falla_sintoma(data: dict = Body(...)):
        falla = data.get("falla")
        if not falla:
            return {
                "success": False,
                "message": "El campo 'falla' es requerido.",
                "code": 400
            }
        sintoma = data.get("sintoma")
        if not sintoma:
            return {
                "success": False,
                "message": "El campo 'sintoma' es requerido.",
                "code": 400
            }
        return service.conectar_falla_sintoma(falla, sintoma)

    @router.post("/recomendacion_falla", summary="Adjudicar sintoma a falla")
    def conectar_falla_sintoma(data: dict = Body(...)):
        recomendacion = data.get("recomendacion")
        if not recomendacion:
            return {
                "success": False,
                "message": "El campo 'recomendacion' es requerido.",
                "code": 400
            }
        falla = data.get("falla")
        if not falla:
            return {
                "success": False,
                "message": "El campo 'falla' es requerido.",
                "code": 400
            }
        return service.conectar_recomendacion_falla(recomendacion, falla)

    return router