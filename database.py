import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",      # Cambiar si el servidor no está local
        user="tu_usuario",     # Reemplazar por tu usuario MySQL
        password="tu_password", # Reemplazar por tu contraseña MySQL
        database="proyectoX"
    )

