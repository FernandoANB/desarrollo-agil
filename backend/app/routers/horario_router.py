from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import time
from app.schemas.horario import Horario, HorarioCreate, HorarioUpdate
from app.services import horario_service
from app.database import get_db

router = APIRouter(prefix="/horarios", tags=["horarios"])

@router.get("/", response_model=List[Horario])
def get_horarios(db: Session = Depends(get_db)):
    return horario_service.get_all_horarios(db)

@router.get("/empresa/{id_empresa}", response_model=List[Horario])
def get_horarios_empresa(id_empresa: int, db: Session = Depends(get_db)):
    """Obtiene todos los horarios configurados para una empresa (US-13)"""
    return horario_service.get_horarios_por_empresa(db, id_empresa)

@router.get("/empresa/{id_empresa}/cerrados", response_model=List[Horario])
def get_dias_cerrados(id_empresa: int, db: Session = Depends(get_db)):
    """Obtiene los días cerrados de una empresa (US-13)"""
    return horario_service.get_dias_cerrados(db, id_empresa)

@router.get("/empresa/{id_empresa}/dia/{dia_semana}", response_model=Horario)
def get_horario_por_dia(id_empresa: int, dia_semana: int, db: Session = Depends(get_db)):
    """Obtiene la configuración de horario para un día específico (US-13)"""
    horario = horario_service.get_horario_por_dia(db, id_empresa, dia_semana)
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado para ese día")
    return horario

@router.get("/empresa/{id_empresa}/verificar", response_model=dict)
def verificar_horario(
    id_empresa: int,
    dia_semana: int = Query(..., ge=0, le=6),
    hora: time = Query(...),
    db: Session = Depends(get_db)
):
    """Verifica si un horario está disponible para hacer reserva (US-13)"""
    disponible = horario_service.verificar_horario_disponible(db, id_empresa, dia_semana, hora)
    return {"disponible": disponible, "dia_semana": dia_semana, "hora": hora}

@router.get("/{id_horario}", response_model=Horario)
def get_horario(id_horario: int, db: Session = Depends(get_db)):
    horario = horario_service.get_horario(db, id_horario)
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return horario

@router.post("/", response_model=Horario)
def create_horario(horario: HorarioCreate, db: Session = Depends(get_db)):
    return horario_service.create_horario(db, horario)

@router.put("/{id_horario}", response_model=Horario)
def update_horario(id_horario: int, horario: HorarioUpdate, db: Session = Depends(get_db)):
    updated_horario = horario_service.update_horario(db, id_horario, horario)
    if not updated_horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return updated_horario

@router.delete("/{id_horario}")
def delete_horario(id_horario: int, db: Session = Depends(get_db)):
    if not horario_service.delete_horario(db, id_horario):
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return {"detail": "Horario eliminado"}
