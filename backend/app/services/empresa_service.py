from sqlalchemy.orm import Session
from app.models.models import Empresa
from app.schemas.empresa import EmpresaCreate, EmpresaUpdate

def get_all_empresas(db: Session):
    return db.query(Empresa).all()

def get_empresas_activas(db: Session):
    """Obtiene solo las empresas activas (US-14)"""
    return db.query(Empresa).filter(Empresa.activa == True).all()

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

def update_marca_empresa(db: Session, empresa_id: int, logo_url: str = None, 
                          color_primario: str = None, color_secundario: str = None, 
                          fotos_urls: str = None):
    """Actualiza los datos de marca/branding de una empresa (US-14)"""
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa:
        if logo_url is not None:
            db_empresa.logo_url = logo_url
        if color_primario is not None:
            db_empresa.color_primario = color_primario
        if color_secundario is not None:
            db_empresa.color_secundario = color_secundario
        if fotos_urls is not None:
            db_empresa.fotos_urls = fotos_urls
        db.commit()
        db.refresh(db_empresa)
    return db_empresa

def delete_empresa(db: Session, empresa_id: int):
    db_empresa = db.query(Empresa).filter(Empresa.id_empresa == empresa_id).first()
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
    return db_empresa
