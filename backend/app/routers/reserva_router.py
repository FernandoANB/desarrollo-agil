import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.schemas.reserva import Reserva, ReservaCreate, ReservaUpdate
from app.services import reserva_service, fecha_bloqueada_service, horario_service, servicio_service
from app.database import get_db

# ¡ESTA LÍNEA ES VITAL! Es la que repara tu error 'AttributeError' en main.py
router = APIRouter(prefix="/reservas", tags=["reservas"])

# --- FUNCIÓN PARA ENVIAR EL CORREO REAL DESDE PYTHON ---
def enviar_correo_confirmacion(email_destinatario: str, nombre: str, fecha: str, hora: str, personas: int, notas: str):
    # Lee las variables ocultas de tu archivo .env
    remitente = os.environ.get("SMTP_USER", "fernandonunezbetancur@gmail.com")
    password = os.environ.get("SMTP_PASSWORD", "tqge bzft kwwb zrru")
    
    try:
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = email_destinatario
        msg['Subject'] = "Confirmación de Reserva - Reserva Refinada ✨"
        
        # Formato del correo
        cuerpo = f"""
        ¡Hola {nombre}!
        
        Tu reserva ha sido procesada exitosamente. Aquí tienes los detalles:
        
        - Fecha: {fecha}
        - Hora: {hora}
        - Cantidad de invitados: {personas}
        - Notas adicionales: {notas if notas else 'Ninguna'}
        
        ¡Te esperamos pronto para una experiencia inolvidable!
        """
        
        msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))
        
        # Conexión con el servidor de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.sendmail(remitente, email_destinatario, msg.as_string())
        server.quit()
        
        print(f"✅ ¡ÉXITO! Correo enviado a {email_destinatario}")
    except Exception as e:
        print(f"❌ Error al intentar enviar el correo: {e}")
        print("⚠️ (Simulando envío para continuar con la demo)")

# --- ENDPOINTS ---

@router.get("/", response_model=List[Reserva])
def get_reservas(db: Session = Depends(get_db)):
    return reserva_service.get_all_reservas(db)

@router.get("/{id_reserva}", response_model=Reserva)
def get_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva = reserva_service.get_reserva(db, id_reserva)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva

@router.post("/", response_model=Reserva)
def create_reserva(reserva: ReservaCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # --- VALIDACIONES US-12 y US-13 ---
    
    # Obtener el servicio para acceder a la empresa
    servicio = servicio_service.get_servicio(db, reserva.id_servicio)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    
    # Validar que la fecha NO esté bloqueada (US-12)
    if fecha_bloqueada_service.verificar_fecha_bloqueada(db, servicio.id_empresa, reserva.fecha):
        raise HTTPException(
            status_code=400, 
            detail="Esta fecha está bloqueada. Por favor selecciona otra fecha."
        )
    
    # Validar que el horario sea válido (US-13)
    # Calcular día de semana: 0=Lunes, 6=Domingo
    dia_semana = reserva.fecha.weekday()
    if not horario_service.verificar_horario_disponible(db, servicio.id_empresa, dia_semana, reserva.hora):
        raise HTTPException(
            status_code=400, 
            detail="El horario seleccionado no está disponible. Verifica los horarios de apertura."
        )
    
    # --- CREAR RESERVA ---
    
    # 1. Guarda la reserva en la base de datos
    nueva_reserva = reserva_service.create_reserva(db, reserva)
    
    # 2. Le dice a Python que envíe el correo "en el fondo" sin hacer esperar al usuario
    background_tasks.add_task(
        enviar_correo_confirmacion,
        email_destinatario=nueva_reserva.email_cliente,
        nombre=nueva_reserva.nombre_cliente,
        fecha=str(nueva_reserva.fecha),
        hora=str(nueva_reserva.hora),
        personas=nueva_reserva.cantidad_personas,
        notas=nueva_reserva.notas
    )
    
    return nueva_reserva

@router.put("/{id_reserva}", response_model=Reserva)
def update_reserva(id_reserva: int, reserva: ReservaUpdate, db: Session = Depends(get_db)):
    updated_reserva = reserva_service.update_reserva(db, id_reserva, reserva)
    if not updated_reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return updated_reserva

@router.delete("/{id_reserva}")
def delete_reserva(id_reserva: int, db: Session = Depends(get_db)):
    if not reserva_service.delete_reserva(db, id_reserva):
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return {"detail": "Reserva eliminada"}