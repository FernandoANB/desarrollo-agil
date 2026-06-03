from sqlalchemy.orm import Session
from app.models.models import Empresa
from app.schemas.empresa import EmpresaCreate, EmpresaUpdate

def get_all_empresas(db: Session):
    return db.query(Empresa).all()

def get_empresa(db: Session, empresa_id: int):
    return db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()

def create_empresa(db: Session, empresa: EmpresaCreate):
    db_empresa = Empresa(**empresa.model_dump())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def update_empresa(db: Session, empresa_id: int, empresa: EmpresaUpdate):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa:
        for key, value in empresa.model_dump(exclude_unset=True).items():
            setattr(db_empresa, key, value)
        db.commit()
        db.refresh(db_empresa)
    return db_empresa

def delete_empresa(db: Session, empresa_id: int):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
    return db_empresa
