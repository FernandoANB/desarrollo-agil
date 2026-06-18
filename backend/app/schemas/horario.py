from datetime import time
from typing import Optional
from pydantic import BaseModel, Field

class HorarioBase(BaseModel):
    id_empresa: int
    dia_semana: int = Field(..., ge=0, le=6, description="Día de la semana: 0 (Lunes) a 6 (Domingo)")
    hora_inicio: time
    hora_fin: time
    # Para US-13: Configuración de horarios
    abierto: bool = True
    descripcion: Optional[str] = None

class HorarioCreate(HorarioBase):
    pass

class HorarioUpdate(BaseModel):
    id_empresa: Optional[int] = None
    dia_semana: Optional[int] = Field(None, ge=0, le=6)
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    abierto: Optional[bool] = None
    descripcion: Optional[str] = None

class Horario(HorarioBase):
    id_horario: int

    class Config:
        from_attributes = True
