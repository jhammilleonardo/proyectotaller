from db.database import conectar

# Usuarios
def registrar_usuario(nombre, correo, contraseña):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuarios (nombre, correo, contraseña)
            VALUES (%s, %s, %s)
        """, (nombre, correo, contraseña))
        conexion.commit()
        print("Usuario registrado exitosamente.")
    except Exception as e:
        print("Error al registrar usuario:", e)
    finally:
        cursor.close()
        conexion.close()

# Publicaciones
def crear_publicacion(id_usuario, contenido, imagen_url=None):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO publicaciones (id_usuario, contenido, imagen_url)
            VALUES (%s, %s, %s)
        """, (id_usuario, contenido, imagen_url))
        conexion.commit()
        print("Publicación creada exitosamente.")
    except Exception as e:
        print("Error al crear publicación:", e)
    finally:
        cursor.close()
        conexion.close()

# Comentarios
def comentar_publicacion(id_publicacion, id_usuario, comentario):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO comentarios (id_publicacion, id_usuario, comentario)
            VALUES (%s, %s, %s)
        """, (id_publicacion, id_usuario, comentario))
        conexion.commit()
        print("Comentario agregado exitosamente.")
    except Exception as e:
        print("Error al agregar comentario:", e)
    finally:
        cursor.close()
        conexion.close()

# Likes
def dar_like(id_publicacion, id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO likes (id_publicacion, id_usuario)
            VALUES (%s, %s)
        """, (id_publicacion, id_usuario))
        conexion.commit()
        print("Like agregado exitosamente.")
    except Exception as e:
        print("Error al dar like:", e)
    finally:
        cursor.close()
        conexion.close()

# Seguidores
def seguir_usuario(id_seguidor, id_seguido):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO seguidores (id_seguidor, id_seguido)
            VALUES (%s, %s)
        """, (id_seguidor, id_seguido))
        conexion.commit()
        print("Ahora sigues al usuario.")
    except Exception as e:
        print("Error al seguir usuario:", e)
    finally:
        cursor.close()
        conexion.close()

# Mensajes
def enviar_mensaje(id_emisor, id_receptor, contenido):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO mensajes (id_emisor, id_receptor, contenido)
            VALUES (%s, %s, %s)
        """, (id_emisor, id_receptor, contenido))
        conexion.commit()
        print("Mensaje enviado exitosamente.")
    except Exception as e:
        print("Error al enviar mensaje:", e)
    finally:
        cursor.close()
        conexion.close()
