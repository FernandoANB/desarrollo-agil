from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.fecha_bloqueada import FechaBloqueada, FechaBloqueadaCreate, FechaBloqueadaUpdate
from app.services import fecha_bloqueada_service
from app.database import get_db

router = APIRouter(prefix="/fechas_bloqueadas", tags=["fechas_bloqueadas"])

@router.get("/", response_model=List[FechaBloqueada])
def get_fechas_bloqueadas(db: Session = Depends(get_db)):
    return fecha_bloqueada_service.get_all_fechas_bloqueadas(db)

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
