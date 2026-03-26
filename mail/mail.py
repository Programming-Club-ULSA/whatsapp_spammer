# -------------------------------------------------------------------------
# NOTA DE IMPLEMENTACIÓN: SERVICIO DE CORREO (SMTP)
# -------------------------------------------------------------------------
# Se ha seleccionado el servidor SMTP de Google (smtp.gmail.com) para el 
# envío de correos dinámicos. Esta elección busca evitar las limitaciones 
# de volumen y costos de suscripción de APIs de terceros (como Resend o 
# SendGrid), permitiendo una integración gratuita y escalable para el club.
#
# REQUISITOS DE CONFIGURACIÓN:
# 1. El remitente debe tener activada la "Verificación en 2 pasos".
# 2. Es NECESARIO generar una "Contraseña de Aplicación" desde la cuenta 
#    de Google (Seguridad > Contraseñas de aplicaciones). 
#    NO se debe usar la contraseña personal por motivos de seguridad y 
#    protocolos modernos de autenticación.
# -------------------------------------------------------------------------

import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def enviar_correo_bienvenida(mail_to_message, userName):
    REMITENTE = os.getenv("SenderMail")
    PASSWORD = os.getenv("AplicationPassword")
    SERVIDOR_SMTP = os.getenv("SERVIDOR_SMTP", "smtp.gmail.com")
    
    try:
        PUERTO = int(os.getenv("PUERTO", 587))
    except (ValueError, TypeError):
        PUERTO = 587

    if not REMITENTE or not PASSWORD:
        print("Error: Las variables de entorno SenderMail o AplicationPassword no están configuradas.")
        return

    try:
        with open('mail\\template.html', 'r', encoding='utf-8') as archivo:
            template_page = archivo.read()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'template.html'. Asegúrate de que esté en la raíz del proyecto.")
        return

    final_html = template_page.replace("{nombre}", userName)

    mensaje = EmailMessage()
    mensaje["Subject"] = "¡Bienvenido al Club de Programación ULSA! 🚀"
    mensaje["From"] = REMITENTE
    mensaje["To"] = mail_to_message
    
    mensaje.set_content("Por favor, activa la vista HTML en tu correo para ver este mensaje.")
    mensaje.add_alternative(final_html, subtype='html')

    try:
        print(f"Conectando a {SERVIDOR_SMTP}:{PUERTO} para enviar a {mail_to_message}...")
        with smtplib.SMTP(SERVIDOR_SMTP, PUERTO) as servidor:
            servidor.starttls() 
            servidor.login(REMITENTE, PASSWORD)
            servidor.send_message(mensaje)
            print(f"¡Correo enviado con éxito a {userName}! 🎉")
            
    except smtplib.SMTPAuthenticationError:
        print("Error de Autenticación: Verifica que 'AplicationPassword' sea correcto y tengas activa la Verificación en 2 pasos.")
    except Exception as e:
        print(f"Hubo un error inesperado al enviar el correo: {e}")