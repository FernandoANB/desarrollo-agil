from sqlalchemy.orm import Session
from datetime import date
from app.models.models import FechaBloqueada
from app.schemas.fecha_bloqueada import FechaBloqueadaCreate, FechaBloqueadaUpdate

def get_all_fechas_bloqueadas(db: Session):
    return db.query(FechaBloqueada).all()

def get_fechas_bloqueadas_por_empresa(db: Session, id_empresa: int):
    """Obtiene todas las fechas bloqueadas para una empresa específica (US-12)"""
    return db.query(FechaBloqueada).filter(FechaBloqueada.id_empresa == id_empresa).all()

def get_fechas_bloqueadas_por_rango(db: Session, id_empresa: int, fecha_inicio: date, fecha_fin: date):
    """Obtiene fechas bloqueadas en un rango de fechas para una empresa (US-12)"""
    return db.query(FechaBloqueada).filter(
        FechaBloqueada.id_empresa == id_empresa,
        FechaBloqueada.fecha >= fecha_inicio,
        FechaBloqueada.fecha <= fecha_fin
    ).all()

def verificar_fecha_bloqueada(db: Session, id_empresa: int, fecha: date) -> bool:
    """Verifica si una fecha está bloqueada para una empresa (US-12)"""
    return db.query(FechaBloqueada).filter(
        FechaBloqueada.id_empresa == id_empresa,
        FechaBloqueada.fecha == fecha
    ).first() is not None

def get_fecha_bloqueada(db: Session, bloqueo_id: int):
    return db.query(FechaBloqueada).filter(FechaBloqueada.id_bloqueo == bloqueo_id).first()

def create_fecha_bloqueada(db: Session, fecha_bloqueada: FechaBloqueadaCreate):
    db_fecha_bloqueada = FechaBloqueada(**fecha_bloqueada.model_dump())
    db.add(db_fecha_bloqueada)
    db.commit()
    db.refresh(db_fecha_bloqueada)
    return db_fecha_bloqueada

def update_fecha_bloqueada(db: Session, bloqueo_id: int, fecha_bloqueada: FechaBloqueadaUpdate):
    db_fecha_bloqueada = db.query(FechaBloqueada).filter(FechaBloqueada.id_bloqueo == bloqueo_id).first()
    if db_fecha_bloqueada:
        for key, value in fecha_bloqueada.model_dump(exclude_unset=True).items():
            setattr(db_fecha_bloqueada, key, value)
        db.commit()
        db.refresh(db_fecha_bloqueada)
    return db_fecha_bloqueada

def delete_fecha_bloqueada(db: Session, bloqueo_id: int):
    db_fecha_bloqueada = db.query(FechaBloqueada).filter(FechaBloqueada.id_bloqueo == bloqueo_id).first()
    if db_fecha_bloqueada:
        db.delete(db_fecha_bloqueada)
        db.commit()
    return db_fecha_bloqueada
