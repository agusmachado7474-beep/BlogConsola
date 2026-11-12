from blog import posts, mostrar_menu, validar_post
from blog import listar_posts, buscar_por_titulo, filtrar_por_tag


# Punto de entrada principal del programa
if __name__ == "__main__":

    while True:

        opcion = mostrar_menu()

        if opcion is None:
            continue

        elif opcion == 1:

            listar_posts(posts)

        elif opcion == 2:

            termino = input("Ingrese el título que desea buscar: ")

            resultados = buscar_por_titulo(posts, termino)

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron publicaciones.")

        elif opcion == 3:

            tag = input("Ingrese el tag que desea buscar: ")

            resultados = filtrar_por_tag(posts, tag)

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron publicaciones con ese tag.")

        elif opcion == 4:

            print("\n===== RESULTADO DE VALIDACIÓN =====")

            for post in posts:

                valido, mensaje = validar_post(post)

                if valido:
                    print("Post ID:", post.get("id"), "- POST VÁLIDO")
                else:
                    print(
                        "Post ID:",
                        post.get("id"),
                        "- POST INVÁLIDO ->",
                        mensaje
                    )

        elif opcion == 5:

            print("Gracias por utilizar el sistema de blog.")
            break

        else:

            print("Opción incorrecta. Elegí un número del 1 al 5.")