from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.base import Base
from app.models import models
from app.routers import (
    empresa_router,
    usuario_router,
    servicio_router,
    horario_router,
    fecha_bloqueada_router,
    reserva_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas SaaS")

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción cambiar por la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(empresa_router.router)
app.include_router(usuario_router.router)
app.include_router(servicio_router.router)
app.include_router(horario_router.router)
app.include_router(fecha_bloqueada_router.router)
app.include_router(reserva_router.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al API de Gestión de Reservas"}
