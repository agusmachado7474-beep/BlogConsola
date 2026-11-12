Sistema de Blog por Consola

Aplicación interactiva por consola desarrollada en Python que permite gestionar y consultar publicaciones de un blog. Este proyecto se realizo con el objetivo de crear una arquitectura modular utilizando paquetes, separación de responsabilidades e importaciones limpias.

Funcionalidades Principales

A través de un menú interactivo por consola, el sistema permite:

* Ver todos los posts: Lista las publicaciones cargadas mostrando su título, autor y estado.
* Buscar por título: Filtra publicaciones mediante coincidencias parciales o totales (sin distinguir mayúsculas o minúsculas).
* Filtrar por tag: Muestra únicamente los posts asociados a una etiqueta específica.
* Validar posts: Verifica que cada publicación cumpla con la estructura de datos requerida (claves obligatorias, tipos de datos, autor anidado y estado válido).
* Salir Finaliza la ejecución del programa de forma controlada.


## Estructura del proyecto

* **blog_consola/** (Carpeta raíz del proyecto)
  * `main.py`: Archivo principal de ejecución y orquestación.
  * `README.md`: Documentación del proyecto.
  * **blog/** (Paquete principal del sistema)
    * `__init__.py`: Inicializador del paquete Python.
    * `datos.py`: Estructuras de datos base del blog.
    * `menu.py`: Interfaz por consola y captura de opciones.
    * `operaciones.py`: Lógica de listado, búsqueda y filtrado.
    * `validaciones.py`: Reglas de validación de estructura y contenido.
