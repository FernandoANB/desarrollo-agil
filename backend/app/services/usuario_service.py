from sqlalchemy.orm import Session
from app.models.models import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate

def get_all_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.model_dump())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if db_usuario:
        for key, value in usuario.model_dump(exclude_unset=True).items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
