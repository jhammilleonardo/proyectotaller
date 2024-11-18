from db.models import registrar_usuario, crear_publicacion, comentar_publicacion, dar_like, seguir_usuario, enviar_mensaje

def menu():
    while True:
        print("\n--- Menú ProyectoX ---")
        print("1. Registrar usuario")
        print("2. Crear publicación")
        print("3. Comentar publicación")
        print("4. Dar like a una publicación")
        print("5. Seguir a un usuario")
        print("6. Enviar mensaje")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            registrar_usuario(nombre, correo, contraseña)
        elif opcion == "2":
            id_usuario = int(input("ID del usuario: "))
            contenido = input("Contenido: ")
            imagen_url = input("URL de la imagen (opcional): ") or None
            crear_publicacion(id_usuario, contenido, imagen_url)
        elif opcion == "3":
            id_publicacion = int(input("ID de la publicación: "))
            id_usuario = int(input("ID del usuario: "))
            comentario = input("Comentario: ")
            comentar_publicacion(id_publicacion, id_usuario, comentario)
        elif opcion == "4":
            id_publicacion = int(input("ID de la publicación: "))
            id_usuario = int(input("ID del usuario: "))
            dar_like(id_publicacion, id_usuario)
        elif opcion == "5":
            id_seguidor = int(input("ID del seguidor: "))
            id_seguido = int(input("ID del seguido: "))
            seguir_usuario(id_seguidor, id_seguido)
        elif opcion == "6":
            id_emisor = int(input("ID del emisor: "))
            id_receptor = int(input("ID del receptor: "))
            contenido = input("Contenido del mensaje: ")
            enviar_mensaje(id_emisor, id_receptor, contenido)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
