from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from app.schemas.fecha_bloqueada import FechaBloqueada, FechaBloqueadaCreate, FechaBloqueadaUpdate
from app.services import fecha_bloqueada_service
from app.database import get_db

router = APIRouter(prefix="/fechas_bloqueadas", tags=["fechas_bloqueadas"])

@router.get("/", response_model=List[FechaBloqueada])
def get_fechas_bloqueadas(db: Session = Depends(get_db)):
    return fecha_bloqueada_service.get_all_fechas_bloqueadas(db)

@router.get("/empresa/{id_empresa}", response_model=List[FechaBloqueada])
def get_fechas_bloqueadas_empresa(id_empresa: int, db: Session = Depends(get_db)):
    """Obtiene todas las fechas bloqueadas para una empresa (US-12)"""
    return fecha_bloqueada_service.get_fechas_bloqueadas_por_empresa(db, id_empresa)

@router.get("/empresa/{id_empresa}/rango", response_model=List[FechaBloqueada])
def get_fechas_bloqueadas_rango(
    id_empresa: int,
    fecha_inicio: date = Query(...),
    fecha_fin: date = Query(...),
    db: Session = Depends(get_db)
):
    """Obtiene fechas bloqueadas en un rango para una empresa (US-12)"""
    return fecha_bloqueada_service.get_fechas_bloqueadas_por_rango(db, id_empresa, fecha_inicio, fecha_fin)

@router.get("/empresa/{id_empresa}/verificar", response_model=dict)
def verificar_fecha_bloqueada(id_empresa: int, fecha: date = Query(...), db: Session = Depends(get_db)):
    """Verifica si una fecha está bloqueada (US-12)"""
    bloqueada = fecha_bloqueada_service.verificar_fecha_bloqueada(db, id_empresa, fecha)
    return {"fecha": fecha, "bloqueada": bloqueada}

@router.get("/{id_bloqueo}", response_model=FechaBloqueada)
def get_fecha_bloqueada(id_bloqueo: int, db: Session = Depends(get_db)):
    fecha_bloqueada = fecha_bloqueada_service.get_fecha_bloqueada(db, id_bloqueo)
    if not fecha_bloqueada:
        raise HTTPException(status_code=404, detail="Fecha bloqueada no encontrada")
    return fecha_bloqueada

@router.post("/", response_model=FechaBloqueada)
def create_fecha_bloqueada(fecha_bloqueada: FechaBloqueadaCreate, db: Session = Depends(get_db)):
    return fecha_bloqueada_service.create_fecha_bloqueada(db, fecha_bloqueada)

@router.put("/{id_bloqueo}", response_model=FechaBloqueada)
def update_fecha_bloqueada(id_bloqueo: int, fecha_bloqueada: FechaBloqueadaUpdate, db: Session = Depends(get_db)):
    updated_fecha = fecha_bloqueada_service.update_fecha_bloqueada(db, id_bloqueo, fecha_bloqueada)
    if not updated_fecha:
        raise HTTPException(status_code=404, detail="Fecha bloqueada no encontrada")
    return updated_fecha

@router.delete("/{id_bloqueo}")
def delete_fecha_bloqueada(id_bloqueo: int, db: Session = Depends(get_db)):
    if not fecha_bloqueada_service.delete_fecha_bloqueada(db, id_bloqueo):
        raise HTTPException(status_code=404, detail="Fecha bloqueada no encontrada")
    return {"detail": "Fecha bloqueada eliminada"}
