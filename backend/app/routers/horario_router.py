from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.horario import Horario, HorarioCreate, HorarioUpdate
from app.services import horario_service
from app.database import get_db

router = APIRouter(prefix="/horarios", tags=["horarios"])

@router.get("/", response_model=List[Horario])
def get_horarios(db: Session = Depends(get_db)):
    return horario_service.get_all_horarios(db)

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
