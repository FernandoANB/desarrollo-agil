from sqlalchemy.orm import Session
from app.models.models import FechaBloqueada
from app.schemas.fecha_bloqueada import FechaBloqueadaCreate, FechaBloqueadaUpdate

def get_all_fechas_bloqueadas(db: Session):
    return db.query(FechaBloqueada).all()

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
