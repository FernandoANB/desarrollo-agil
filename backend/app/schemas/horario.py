from datetime import time
from typing import Optional
from pydantic import BaseModel, Field

class HorarioBase(BaseModel):
    id_empresa: int
    dia_semana: int = Field(..., ge=1, le=7, description="Día de la semana: 1 (Lunes) a 7 (Domingo)")
    hora_inicio: time
    hora_fin: time

class HorarioCreate(HorarioBase):
    pass

class HorarioUpdate(BaseModel):
    id_empresa: Optional[int] = None
    dia_semana: Optional[int] = Field(None, ge=1, le=7)
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None

class Horario(HorarioBase):
    id_horario: int

    class Config:
        from_attributes = True
