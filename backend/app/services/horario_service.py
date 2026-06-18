from sqlalchemy.orm import Session
from datetime import time
from app.models.models import Horario
from app.schemas.horario import HorarioCreate, HorarioUpdate

def get_all_horarios(db: Session):
    return db.query(Horario).all()

def get_horarios_por_empresa(db: Session, id_empresa: int):
    """Obtiene todos los horarios configurados para una empresa (US-13)"""
    return db.query(Horario).filter(Horario.id_empresa == id_empresa).order_by(Horario.dia_semana).all()

def get_horario_por_dia(db: Session, id_empresa: int, dia_semana: int):
    """Obtiene la configuración de horario para un día específico (US-13)"""
    return db.query(Horario).filter(
        Horario.id_empresa == id_empresa,
        Horario.dia_semana == dia_semana
    ).first()

def get_dias_cerrados(db: Session, id_empresa: int):
    """Obtiene los días cerrados de una empresa (US-13)"""
    return db.query(Horario).filter(
        Horario.id_empresa == id_empresa,
        Horario.abierto == False
    ).all()

def verificar_horario_disponible(db: Session, id_empresa: int, dia_semana: int, hora: time) -> bool:
    """Verifica si un horario está disponible para hacer reserva (US-13)"""
    horario = get_horario_por_dia(db, id_empresa, dia_semana)
    if not horario:
        return False
    if not horario.abierto:
        return False
    return horario.hora_inicio <= hora <= horario.hora_fin

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
