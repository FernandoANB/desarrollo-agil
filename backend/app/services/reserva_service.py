from sqlalchemy.orm import Session
from app.models.models import Reserva
from app.schemas.reserva import ReservaCreate, ReservaUpdate

def get_all_reservas(db: Session):
    return db.query(Reserva).all()

def get_reserva(db: Session, reserva_id: int):
    return db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()

def create_reserva(db: Session, reserva: ReservaCreate):
    db_reserva = Reserva(**reserva.model_dump())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def update_reserva(db: Session, reserva_id: int, reserva: ReservaUpdate):
    db_reserva = db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()
    if db_reserva:
        for key, value in reserva.model_dump(exclude_unset=True).items():
            setattr(db_reserva, key, value)
        db.commit()
        db.refresh(db_reserva)
    return db_reserva

def delete_reserva(db: Session, reserva_id: int):
    db_reserva = db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()
    if db_reserva:
        db.delete(db_reserva)
        db.commit()
    return db_reserva
