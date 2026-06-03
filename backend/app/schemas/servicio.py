from typing import Optional
from pydantic import BaseModel, Field

class ServicioBase(BaseModel):
    id_empresa: int
    nombre: str
    descripcion: Optional[str] = None
    duracion_minutos: Optional[int] = None
    capacidad_maxima: Optional[int] = Field(default=1, ge=1)
    activo: Optional[bool] = True

class ServicioCreate(ServicioBase):
    pass

class ServicioUpdate(BaseModel):
    id_empresa: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    duracion_minutos: Optional[int] = None
    capacidad_maxima: Optional[int] = Field(default=None, ge=1)
    activo: Optional[bool] = None

class Servicio(ServicioBase):
    id_servicio: int

    class Config:
        from_attributes = True
