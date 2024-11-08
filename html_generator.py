import sqlite3

def obtener_datos_desde_db(db_name='noticias.db'):
    """
    Obtiene los títulos y resúmenes desde la base de datos SQLite.
    """
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('SELECT titulo, resumen FROM noticias')
        rows = c.fetchall()
    except sqlite3.Error as e:
        print("Error al interactuar con la base de datos:", e)
        rows = []
    finally:
        if conn:
            conn.close()
    return rows

def generar_css():
    """
    Genera el contenido CSS para el HTML.
    """
    return '''
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 0; 
            background-color: #f0f2f5; 
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
        }
        h1 {
            color: #222;
            font-size: 2em;
            margin-bottom: 30px;
            text-align: center;
        }
        .navbar {
            background-color: #1f2833;
            color: #ffffff;
            padding: 15px;
            font-size: 1.2em;
            text-align: center;
        }
        .navbar a {
            color: #ffffff;
            text-decoration: none;
            padding: 0 15px;
            transition: color 0.3s;
        }
        .navbar a:hover {
            color: #66fcf1;
        }
        .noticia-container {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .noticia {
            background-color: #ffffff;
            width: 100%;
            padding: 20px;
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
            border-radius: 10px;
            transition: transform 0.4s, box-shadow 0.4s, background-color 0.4s;
        }
        .noticia:hover {
            transform: scale(1.02);
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.25);
            background-color: #e0f7fa;
            color: #1f2833;
            z-index: 10;
        }
        .titulo {
            font-weight: bold;
            font-size: 1.3em;
            color: #333;
            margin-bottom: 10px;
        }
        .resumen {
            font-size: 1em;
            color: #555;
            line-height: 1.6;
        }
    </style>
    '''

def generar_cuerpo_html(rows):
    """
    Genera el cuerpo HTML con los títulos y resúmenes.
    """
    cuerpo_html = '''
    <div class="navbar">
        <a href="#">Inicio</a> |
        <a href="#noticias">Noticias</a> |
        <a href="#">Contacto</a>
    </div>
    <div class="container">
        <h1>Últimas Noticias</h1>
        <div class="noticia-container">
    '''
    for titulo, resumen in rows:
        cuerpo_html += f'''
        <div class="noticia">
            <div class="titulo">{titulo}</div>
            <div class="resumen">{resumen}</div>
        </div>
        '''
    
    cuerpo_html += '''
        </div>
    </div>
    '''
    return cuerpo_html

def generar_html_content(rows):
    """
    Genera el contenido HTML completo combinando el CSS y el cuerpo.
    """
    html_content = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Noticias</title>
        ''' + generar_css() + '''
    </head>
    <body>
    ''' + generar_cuerpo_html(rows) + '''
    </body>
    </html>
    '''
    return html_content

def escribir_html(html_content, html_file='noticias.html'):
    """
    Escribe el contenido HTML en un archivo.
    """
    try:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    except IOError as e:
        print("Error al escribir el archivo HTML:", e)

def generar_html(db_name='noticias.db', html_file='noticias.html'):
    """
    Genera un archivo HTML con los títulos y resúmenes almacenados en la base de datos.
    """
    rows = obtener_datos_desde_db(db_name)
    html_content = generar_html_content(rows)
    escribir_html(html_content, html_file)
