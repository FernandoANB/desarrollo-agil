from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr

class RolEnum(str, Enum):
    ADMIN = "ADMIN"
    OPERADOR = "OPERADOR"
    CLIENTE = "CLIENTE"

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    rol: RolEnum
    id_empresa: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    rol: Optional[RolEnum] = None
    password: Optional[str] = None
    id_empresa: Optional[int] = None

class Usuario(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True
