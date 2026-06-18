from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class EmpresaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    # Campos para US-14: Personalización de Marca
    logo_url: Optional[str] = None
    color_primario: Optional[str] = Field(None, pattern=r"^#[0-9A-Fa-f]{6}$", description="Código HEX: #RRGGBB")
    color_secundario: Optional[str] = Field(None, pattern=r"^#[0-9A-Fa-f]{6}$", description="Código HEX: #RRGGBB")
    fotos_urls: Optional[str] = None  # JSON array de URLs
    activa: Optional[bool] = None

class Empresa(EmpresaBase):
    id_empresa: int
    logo_url: Optional[str] = None
    color_primario: Optional[str] = None
    color_secundario: Optional[str] = None
    fotos_urls: Optional[str] = None
    activa: bool

    class Config:
        from_attributes = True
