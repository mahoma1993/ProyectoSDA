import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración para SMTP
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
smtp_encryption = 'STARTTLS'
ccorreo_emisor = 'mierarpi2024@hotmail.com'
contrasena_correo = 'yrxputkygbrjapbp'  # Reemplaza con la contraseña de aplicación generada

# Mensaje a enviar
mensaje = MIMEMultipart()
mensaje['From'] = ccorreo_emisor
mensaje['To'] = 'mohamed_hamudi@hotmail.com'
mensaje['Subject'] = 'Temperatura alta'
mensaje.attach(MIMEText("La temperatura actual °C supera la temperatura establecida °C).", 'plain'))

# Configuración de contexto SSL para SMTP
context_smtp = ssl.create_default_context()

try:
    # Enviar correo utilizando SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context_smtp)
        server.login(ccorreo_emisor, contrasena_correo)
        server.sendmail(ccorreo_emisor, 'mohamed_hamudi@hotmail.com', mensaje.as_string())
        print("Correo enviado exitosamente.")

except Exception as e:
    print(f"Error al enviar el correo: {e}")

