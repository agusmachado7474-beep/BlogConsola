# Datos del autor del blog
perfil_autor = {
    "nombre": "Agustín Machado",
    "bio": "Desarrollador web",
    "especialidad": "Python y Java",
    "redes_sociales": ["@Amachado", "@AgusPython"]
}
# Estados permitidos para las publicaciones
estados_post = ("borrador", "publicado", "archivado")
# Tags disponibles en el blog
etiquetas_blog = {
    "Python", "Django", "Web", "Backend",
    "Principiantes", "Inteligencia Artificial", "Finanzas"
}
# Lista de publicaciones del blog
posts = [
    {
        "id": 100,
        "titulo": "Primeros pasos con Python",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 101,
        "titulo": "El futuro de la Inteligencia Artificial",
        "autor": perfil_autor,
        "tags": ["Inteligencia Artificial", "Principiantes"],
        "estado": "borrador"
    },
    {
        "id": 103,
        "titulo": "Python para analistas financieros",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes", "Finanzas"],
        "estado": "publicado"
    },
    {
        "id": 104,
        "titulo": "",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "publicado"
    }
]
