from typing import Optional
from pydantic import BaseModel, EmailStr

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

class Empresa(EmpresaBase):
    id_empresa: int

    class Config:
        from_attributes = True
