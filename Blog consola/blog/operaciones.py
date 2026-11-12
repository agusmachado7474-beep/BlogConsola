# Muestra los posts de una lista
def listar_posts(lista):

    if not lista:
        print("No hay publicaciones para mostrar.")
        return

    for post in lista:
        print("----------------------")
        print("ID:", post.get("id"))
        print("Título:", post.get("titulo"))
        print("Autor:", post.get("autor", {}).get("nombre"))
        print("Estado:", post.get("estado"))
        print("Tags:", post.get("tags"))

# Busca publicaciones por título
def buscar_por_titulo(lista, termino):

    resultados = []

    for post in lista:

        titulo = post.get("titulo", "")

        if termino.lower() in titulo.lower():
            resultados.append(post)

    return resultados


# Filtra publicaciones por una etiqueta
def filtrar_por_tag(lista, tag):

    resultados = []

    for post in lista:

        for etiqueta in post.get("tags", []):

            if etiqueta.lower() == tag.lower():
                resultados.append(post)
                break

    return resultados

