# Muestra el menú principal y devuelve una opción
def mostrar_menu():

    print("\n===== MENÚ DEL BLOG =====")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Introducí el número de la opción: "))
        return opcion

    except ValueError:
        print("Error: tenés que ingresar un número.")
        return None