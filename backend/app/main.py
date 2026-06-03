from fastapi import FastAPI
from app.routers import (
    empresa_router,
    usuario_router,
    servicio_router,
    horario_router,
    fecha_bloqueada_router,
    reserva_router
)

app = FastAPI(title="Sistema de Reservas SaaS")

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
