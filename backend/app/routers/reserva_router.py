import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv() # Carga las credenciales del .env de forma segura

def enviar_correo_real_confirmacion(email_destinatario: str, fecha: str, hora: str):
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    
    if not user or not password:
        print("⚠️ Variables SMTP no detectadas. Simulación en consola activada.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = email_destinatario
        msg['Subject'] = "Tu Reserva en Reserva Refinada está Confirmada ✨"
        
        cuerpo = f"¡Hola! Tu mesa para el {fecha} a las {hora} ha sido reservada con éxito."
        msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))
        
        server = smtplib.SMTP(os.getenv("SMTP_SERVER", "smtp.gmail.com"), int(os.getenv("SMTP_PORT", 587)))
        server.starttls()
        server.login(user, password)
        server.sendmail(user, email_destinatario, msg.as_string())
        server.quit()
        print("📧 ¡Correo real despachado con éxito!")
    except Exception as e:
        print(f"❌ Error al enviar correo SMTP: {str(e)}")