from sqlalchemy.orm import Session
from app.models.models import Horario
from app.schemas.horario import HorarioCreate, HorarioUpdate

def get_all_horarios(db: Session):
    return db.query(Horario).all()

def get_horario(db: Session, horario_id: int):
    return db.query(Horario).filter(Horario.id_horario == horario_id).first()

def create_horario(db: Session, horario: HorarioCreate):
    db_horario = Horario(**horario.model_dump())
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario

def update_horario(db: Session, horario_id: int, horario: HorarioUpdate):
    db_horario = db.query(Horario).filter(Horario.id_horario == horario_id).first()
    if db_horario:
        for key, value in horario.model_dump(exclude_unset=True).items():
            setattr(db_horario, key, value)
        db.commit()
        db.refresh(db_horario)
    return db_horario

def delete_horario(db: Session, horario_id: int):
    db_horario = db.query(Horario).filter(Horario.id_horario == horario_id).first()
    if db_horario:
        db.delete(db_horario)
        db.commit()
    return db_horario
