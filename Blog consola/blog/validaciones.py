from blog.datos import estados_post, etiquetas_blog

# Valida que un post tenga la estructura correcta
def validar_post(post):

    if not isinstance(post, dict):
        return False, "No es un diccionario"

    claves = ["id", "titulo", "autor", "tags", "estado"]

    for clave in claves:
        if clave not in post:
            return False, f"Falta la clave {clave}"

    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "Título vacío"

    if post["estado"] not in estados_post:
        return False, "Estado inválido"

    if not isinstance(post["autor"], dict):
        return False, "Autor inválido"

    if not isinstance(post["tags"], list) or not post["tags"]:
        return False, "Tags inválidos"

    for tag in post["tags"]:
        if tag not in etiquetas_blog:
            return False, f"Tag inválido: {tag}"

    return True, "Correcto"
