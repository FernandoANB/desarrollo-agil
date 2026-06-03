from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.servicio import Servicio, ServicioCreate, ServicioUpdate
from app.services import servicio_service
from app.database import get_db

router = APIRouter(prefix="/servicios", tags=["servicios"])

@router.get("/", response_model=List[Servicio])
def get_servicios(db: Session = Depends(get_db)):
    return servicio_service.get_all_servicios(db)

@router.get("/{id_servicio}", response_model=Servicio)
def get_servicio(id_servicio: int, db: Session = Depends(get_db)):
    servicio = servicio_service.get_servicio(db, id_servicio)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio

@router.post("/", response_model=Servicio)
def create_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    return servicio_service.create_servicio(db, servicio)

@router.put("/{id_servicio}", response_model=Servicio)
def update_servicio(id_servicio: int, servicio: ServicioUpdate, db: Session = Depends(get_db)):
    updated_servicio = servicio_service.update_servicio(db, id_servicio, servicio)
    if not updated_servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return updated_servicio

@router.delete("/{id_servicio}")
def delete_servicio(id_servicio: int, db: Session = Depends(get_db)):
    if not servicio_service.delete_servicio(db, id_servicio):
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"detail": "Servicio eliminado"}
