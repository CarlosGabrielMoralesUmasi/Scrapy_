
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

Funcionamiento del Código
-------------------------

**main.py**:
- Importa las funciones necesarias de los otros módulos.
- Define la función `main()`, que coordina todo el proceso:
  - Obtiene los títulos y enlaces de las noticias.
  - Para cada noticia, obtiene el resumen correspondiente.
  - Guarda los datos en la base de datos.
  - Genera el archivo HTML.
- Ejecuta la función `main()` cuando el script es ejecutado directamente.

**scraper.py**:

- `obtener_titulos_y_links(url)`:
  - Envía una solicitud HTTP a la URL proporcionada.
  - Analiza el contenido HTML y extrae los títulos y enlaces de las primeras 10 noticias.
  - Retorna una lista de diccionarios con los títulos y enlaces.

- `obtener_resumen(url)`:
  - Envía una solicitud HTTP a la URL de una noticia específica.
  - Analiza el contenido HTML y extrae el resumen de la noticia.
  - Retorna el resumen como una cadena de texto.

**database.py**:

- `guardar_en_base_de_datos(titulos_y_resumenes, db_name='noticias.db')`:
  - Conecta o crea una base de datos SQLite con el nombre especificado.
  - Crea la tabla `noticias` si no existe.
  - Inserta los títulos y resúmenes en la tabla.
  - Cierra la conexión a la base de datos.

**html_generator.py**:

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
