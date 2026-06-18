from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.empresa import Empresa, EmpresaCreate, EmpresaUpdate
from app.services import empresa_service
from app.database import get_db

router = APIRouter(prefix="/empresas", tags=["empresas"])

@router.get("/", response_model=List[Empresa])
def get_empresas(db: Session = Depends(get_db)):
    return empresa_service.get_all_empresas(db)

@router.get("/activas", response_model=List[Empresa])
def get_empresas_activas(db: Session = Depends(get_db)):
    """Obtiene solo las empresas activas (US-14)"""
    return empresa_service.get_empresas_activas(db)

@router.get("/{id_empresa}", response_model=Empresa)
def get_empresa(id_empresa: int, db: Session = Depends(get_db)):
    empresa = empresa_service.get_empresa(db, id_empresa)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return empresa

@router.post("/", response_model=Empresa)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    return empresa_service.create_empresa(db, empresa)

@router.put("/{id_empresa}", response_model=Empresa)
def update_empresa(id_empresa: int, empresa: EmpresaUpdate, db: Session = Depends(get_db)):
    updated_empresa = empresa_service.update_empresa(db, id_empresa, empresa)
    if not updated_empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return updated_empresa

@router.put("/{id_empresa}/marca", response_model=Empresa)
def update_marca_empresa(
    id_empresa: int,
    logo_url: Optional[str] = Query(None),
    color_primario: Optional[str] = Query(None),
    color_secundario: Optional[str] = Query(None),
    fotos_urls: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """Actualiza los datos de marca/branding de una empresa (US-14)"""
    updated_empresa = empresa_service.update_marca_empresa(
        db, id_empresa, logo_url, color_primario, color_secundario, fotos_urls
    )
    if not updated_empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return updated_empresa

@router.delete("/{id_empresa}")
def delete_empresa(id_empresa: int, db: Session = Depends(get_db)):
    if not empresa_service.delete_empresa(db, id_empresa):
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return {"detail": "Empresa eliminada"}
