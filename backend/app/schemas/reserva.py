from datetime import date, time, datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class EstadoReservaEnum(str, Enum):
    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    FINALIZADA = "FINALIZADA"

class ReservaBase(BaseModel):
    id_servicio: int
    nombre_cliente: str
    email_cliente: EmailStr
    rut: Optional[str] = None
    telefono: Optional[str] = None
    fecha: date
    hora: time
    cantidad_personas: Optional[int] = Field(default=1, ge=1)
    notas: Optional[str] = None
    estado: Optional[EstadoReservaEnum] = EstadoReservaEnum.CONFIRMADA

class ReservaCreate(ReservaBase):
    pass

class ReservaUpdate(BaseModel):
    id_servicio: Optional[int] = None
    nombre_cliente: Optional[str] = None
    email_cliente: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha: Optional[date] = None
    hora: Optional[time] = None
    cantidad_personas: Optional[int] = Field(default=None, ge=1)
    notas: Optional[str] = None
    estado: Optional[EstadoReservaEnum] = None

class Reserva(ReservaBase):
    id_reserva: int
    fecha_creacion: Optional[datetime] = None

    class Config:
        from_attributes = True
