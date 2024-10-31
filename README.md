
Proyecto de Scraping de Noticias de El Comercio
==============================================

Descripción
-----------

Este proyecto realiza un scraping de las últimas noticias del sitio web de El Comercio (https://elcomercio.pe/ultimas-noticias/). Extrae los títulos y resúmenes de las noticias y los almacena en una base de datos SQLite. Además, genera un archivo HTML que muestra de forma legible los títulos y resúmenes extraídos.

Estructura del Proyecto
-----------------------

El proyecto está organizado en varios archivos para mejorar la modularidad y facilitar el mantenimiento:

1. **main.py**: Archivo principal que coordina la ejecución de las funciones.
2. **scraper.py**: Contiene las funciones relacionadas con la obtención de datos de las noticias.
3. **database.py**: Contiene la función para guardar los datos en la base de datos SQLite.
4. **html_generator.py**: Contiene la función para generar el archivo HTML.
5. **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
6. **README.txt**: Este archivo, que proporciona información detallada sobre el proyecto.

Requisitos Previos
------------------

- **Python 3.x**: Asegúrate de tener instalada una versión reciente de Python 3.
- **Paquetes Python**: Se requieren los paquetes `requests` y `beautifulsoup4`.

Instalación de Dependencias
---------------------------

Antes de ejecutar el proyecto, instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

Ejecución del Proyecto
----------------------

Descarga del código: Asegúrate de que todos los archivos del proyecto (main.py, scraper.py, database.py, html_generator.py, requirements.txt, y README.txt) están en el mismo directorio.

Ejecuta el script principal:

En tu terminal o línea de comandos, navega hasta el directorio del proyecto y ejecuta:

```bash
python main.py
```

Resultados:
-----------

- **Base de Datos**: Se creará un archivo `noticias.db` en el directorio actual, que contiene los títulos y resúmenes de las noticias extraídas.
- **Archivo HTML**: Se generará un archivo `noticias.html` que muestra los títulos y resúmenes de forma legible. Puedes abrir este archivo en tu navegador web preferido.

# Funcionamiento del Código
-------------------------

# main.py
- Importa las funciones necesarias de los otros módulos.
- Define la función `main()`, que coordina todo el proceso:
  - Obtiene los títulos y enlaces de las noticias.
  - Para cada noticia, obtiene el resumen correspondiente.
  - Guarda los datos en la base de datos.
  - Genera el archivo HTML.
- Ejecuta la función `main()` cuando el script es ejecutado directamente.

# scraper.py

`scraper.py` es un script de Python diseñado para extraer información de noticias desde una página web. Utiliza `requests` para obtener el contenido HTML de una URL y `BeautifulSoup` para analizar y extraer los datos específicos como títulos, enlaces, y resúmenes de las noticias.

## Funciones Principales

1. **obtener_contenido_pagina(url)**:
   - Realiza una solicitud HTTP a la URL proporcionada y devuelve el contenido HTML si la solicitud es exitosa.
   - Maneja errores HTTP llamando a `manejar_error` y devolviendo `None` en caso de falla.
   
2. **manejar_error(error)**:
   - Imprime un mensaje de error cuando ocurre una falla en la solicitud HTTP.
   - Devuelve `None` como respuesta de error.

3. **extraer_titulos_y_links(soup)**:
   - Toma un objeto `BeautifulSoup` como entrada y encuentra los primeros 10 títulos y enlaces en la estructura HTML.
   - Llama a `procesar_noticia` para procesar cada título y enlace encontrado, devolviendo una lista de diccionarios con esta información.

4. **procesar_noticia(noticia)**:
   - Extrae el título de una noticia y el enlace asociado.
   - Si el enlace es relativo, llama a `construir_url_completa` para convertirlo en una URL absoluta.
   - Devuelve un diccionario con el título y el enlace.

5. **construir_url_completa(enlace)**:
   - Verifica si el enlace es relativo y lo convierte en una URL absoluta usando un URL base.
   - Devuelve la URL completa.

6. **obtener_titulos_y_links(url)**:
   - Función principal para obtener los títulos y enlaces desde la página principal de noticias.
   - Llama a `obtener_contenido_pagina` para obtener el HTML, y si es exitoso, procesa el contenido usando `procesar_contenido_html`.

7. **procesar_contenido_html(contenido_html)**:
   - Crea un objeto `BeautifulSoup` a partir del HTML de la página y llama a `extraer_titulos_y_links` para extraer los títulos y enlaces.
   - Devuelve una lista de títulos y enlaces procesados.

8. **obtener_resumen(url)**:
   - Extrae el resumen de una noticia individual dado su URL.
   - Llama a `obtener_contenido_pagina` y, si tiene éxito, utiliza `procesar_resumen_html` para extraer el resumen.

9. **procesar_resumen_html(contenido_html)**:
   - Procesa el HTML de la página de la noticia, buscando el resumen en etiquetas específicas.
   - Devuelve el resumen encontrado o `Resumen no disponible` si no se encuentra.

10. **extraer_resumen(soup)**:
    - Busca el resumen de la noticia en etiquetas `h2` específicas o en la etiqueta `meta` con el atributo `DC.description`.
    - Devuelve el resumen si se encuentra, o `None` en caso contrario.

# database.py

`database.py` proporciona funciones para gestionar una base de datos SQLite, que almacena títulos y resúmenes de noticias. Permite la conexión a la base de datos, la creación de la tabla de noticias, y la inserción de datos nuevos, reemplazando los datos existentes.

## Funciones Principales

1. **conectar_base_de_datos(db_name='noticias.db')**
   - Establece la conexión con una base de datos SQLite específica.
   - Devuelve la conexión activa o `None` en caso de error.

2. **crear_tabla_si_no_existe(conn)**
   - Crea la tabla `noticias` si no existe en la base de datos.
   - La tabla tiene tres columnas: `id` (clave primaria autoincremental), `titulo`, y `resumen`.

3. **borrar_datos_existentes(conn)**
   - Borra todos los datos en la tabla `noticias`.
   - Reinicia el contador de autoincremento para mantener la consistencia de los IDs.

4. **insertar_datos(conn, titulos_y_resumenes)**
   - Inserta una lista de títulos y resúmenes en la tabla `noticias`.
   - Cada entrada en la lista debe ser un diccionario con las claves `titulo` y `resumen`.

5. **guardar_en_base_de_datos(titulos_y_resumenes, db_name='noticias.db')**
   - Orquesta el flujo completo de guardado: conecta a la base de datos, crea la tabla si es necesario, borra los datos existentes, y luego inserta los nuevos títulos y resúmenes.
   - Cierra la conexión al finalizar.


# html_generator.py

- `generar_html(db_name='noticias.db', html_file='noticias.html')`:
  - Conecta a la base de datos SQLite y recupera los títulos y resúmenes almacenados.
  - Genera un archivo HTML con los datos recuperados.
  - Escribe el archivo HTML en el directorio actual.

Personalización
---------------

- **Cambiar el número de noticias**: Puedes modificar el número de noticias a extraer cambiando el valor en la función `soup.find_all('h2', limit=10)` dentro de `scraper.py`.
- **Cambiar los nombres de archivos**: Puedes cambiar los nombres de la base de datos y del archivo HTML modificando los parámetros `db_name` y `html_file` en las funciones correspondientes.

Consideraciones
---------------

- **Estructura del sitio web**: Si la estructura de la página de El Comercio cambia, es posible que necesites actualizar los selectores en `scraper.py` para que el script siga funcionando correctamente.
- **Respeto a las Políticas del Sitio**: Asegúrate de cumplir con los términos de uso y políticas de scraping del sitio web de El Comercio. Revisa el archivo `robots.txt` y los términos legales para asegurarte de que estás autorizado a extraer información del sitio.
- **Manejo de Errores**: El código incluye manejo básico de excepciones para conexiones fallidas y errores al interactuar con la base de datos. Sin embargo, es recomendable añadir un manejo de errores más robusto para un entorno de producción.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

