from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.reserva import Reserva, ReservaCreate, ReservaUpdate
from app.services import reserva_service
from app.database import get_db

router = APIRouter(prefix="/reservas", tags=["reservas"])

@router.get("/", response_model=List[Reserva])
def get_reservas(db: Session = Depends(get_db)):
    return reserva_service.get_all_reservas(db)

@router.get("/{id_reserva}", response_model=Reserva)
def get_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva = reserva_service.get_reserva(db, id_reserva)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva

@router.post("/", response_model=Reserva)
def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    return reserva_service.create_reserva(db, reserva)

@router.put("/{id_reserva}", response_model=Reserva)
def update_reserva(id_reserva: int, reserva: ReservaUpdate, db: Session = Depends(get_db)):
    updated_reserva = reserva_service.update_reserva(db, id_reserva, reserva)
    if not updated_reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return updated_reserva

@router.delete("/{id_reserva}")
def delete_reserva(id_reserva: int, db: Session = Depends(get_db)):
    if not reserva_service.delete_reserva(db, id_reserva):
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return {"detail": "Reserva eliminada"}
