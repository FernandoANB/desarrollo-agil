from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from app.services import usuario_service
from app.database import get_db

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/", response_model=List[Usuario])
def get_usuarios(db: Session = Depends(get_db)):
    return usuario_service.get_all_usuarios(db)

@router.get("/{id_usuario}", response_model=Usuario)
def get_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = usuario_service.get_usuario(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=Usuario)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.create_usuario(db, usuario)

@router.put("/{id_usuario}", response_model=Usuario)
def update_usuario(id_usuario: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    updated_usuario = usuario_service.update_usuario(db, id_usuario, usuario)
    if not updated_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated_usuario

@router.delete("/{id_usuario}")
def delete_usuario(id_usuario: int, db: Session = Depends(get_db)):
    if not usuario_service.delete_usuario(db, id_usuario):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado"}
