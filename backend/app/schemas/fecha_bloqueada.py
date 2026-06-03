from datetime import date
from typing import Optional
from pydantic import BaseModel

class FechaBloqueadaBase(BaseModel):
    id_empresa: int
    fecha: date
    motivo: Optional[str] = None

class FechaBloqueadaCreate(FechaBloqueadaBase):
    pass

class FechaBloqueadaUpdate(BaseModel):
    id_empresa: Optional[int] = None
    fecha: Optional[date] = None
    motivo: Optional[str] = None

class FechaBloqueada(FechaBloqueadaBase):
    id_bloqueo: int

    class Config:
        from_attributes = True
