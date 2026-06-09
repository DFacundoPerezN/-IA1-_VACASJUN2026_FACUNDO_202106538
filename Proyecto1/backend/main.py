# py -3.10 -m venv venv
# .\venv\Scripts\Activate.ps1
# pip install fastapi uvicorn pyswip
# uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from repositories.prolog_repo import PrologRepo
from controllers.doctor_controller import doctor_router
from services.doctor_service import DoctorService

app = FastAPI(title="API de Doctor Byte")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen (para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, etc.
    allow_headers=["*"],
)

repository = PrologRepo("doctor.pl")

service = DoctorService(repository)

app.include_router(doctor_router(service))