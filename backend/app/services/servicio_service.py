from sqlalchemy.orm import Session
from app.models.models import Servicio
from app.schemas.servicio import ServicioCreate, ServicioUpdate

def get_all_servicios(db: Session):
    return db.query(Servicio).all()

def get_servicio(db: Session, servicio_id: int):
    return db.query(Servicio).filter(Servicio.id_servicio == servicio_id).first()

def create_servicio(db: Session, servicio: ServicioCreate):
    db_servicio = Servicio(**servicio.model_dump())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio(db: Session, servicio_id: int, servicio: ServicioUpdate):
    db_servicio = db.query(Servicio).filter(Servicio.id_servicio == servicio_id).first()
    if db_servicio:
        for key, value in servicio.model_dump(exclude_unset=True).items():
            setattr(db_servicio, key, value)
        db.commit()
        db.refresh(db_servicio)
    return db_servicio

def delete_servicio(db: Session, servicio_id: int):
    db_servicio = db.query(Servicio).filter(Servicio.id_servicio == servicio_id).first()
    if db_servicio:
        db.delete(db_servicio)
        db.commit()
    return db_servicio
