from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Time, Date, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Empresa(Base):
    __tablename__ = "empresas"
    id_empresa = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    direccion = Column(String(255))
    telefono = Column(String(20))
    email = Column(String(100))

    usuarios = relationship("Usuario", back_populates="empresa")
    servicios = relationship("Servicio", back_populates="empresa")
    horarios = relationship("Horario", back_populates="empresa")
    fechas_bloqueadas = relationship("FechaBloqueada", back_populates="empresa")

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255))
    rol = Column(Enum('ADMIN', 'OPERADOR', 'CLIENTE', name='rol_enum'), nullable=False)
    id_empresa = Column(Integer, ForeignKey("empresas.id_empresa"))

    empresa = relationship("Empresa", back_populates="usuarios")

class Servicio(Base):
    __tablename__ = "servicios"
    id_servicio = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(Integer, ForeignKey("empresas.id_empresa"), nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    duracion_minutos = Column(Integer)
    capacidad_maxima = Column(Integer, default=1)
    activo = Column(Boolean, default=True)

    empresa = relationship("Empresa", back_populates="servicios")
    reservas = relationship("Reserva", back_populates="servicio")

class Horario(Base):
    __tablename__ = "horarios"
    id_horario = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(Integer, ForeignKey("empresas.id_empresa"), nullable=False)
    dia_semana = Column(Integer, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)

    empresa = relationship("Empresa", back_populates="horarios")

class FechaBloqueada(Base):
    __tablename__ = "fechas_bloqueadas"
    id_bloqueo = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(Integer, ForeignKey("empresas.id_empresa"), nullable=False)
    fecha = Column(Date, nullable=False)
    motivo = Column(String(255))

    empresa = relationship("Empresa", back_populates="fechas_bloqueadas")

class Reserva(Base):
    __tablename__ = "reservas"
    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    id_servicio = Column(Integer, ForeignKey("servicios.id_servicio"), nullable=False)
    nombre_cliente = Column(String(100), nullable=False)
    email_cliente = Column(String(100), nullable=False)
    rut = Column(String(20))
    telefono = Column(String(20))
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    cantidad_personas = Column(Integer, default=1)
    notas = Column(Text)
    estado = Column(Enum('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'FINALIZADA', name='estado_reserva_enum'), default='CONFIRMADA')
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    servicio = relationship("Servicio", back_populates="reservas")
