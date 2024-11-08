import sqlite3

def conectar_base_de_datos(db_name='noticias.db'):
    """
    Conecta a la base de datos SQLite y devuelve la conexión.
    """
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print("Error al conectar con la base de datos:", e)
        return None

def crear_tabla_si_no_existe(conn):
    """
    Crea la tabla de noticias si no existe.
    """
    try:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS noticias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                resumen TEXT
            )
        ''')
    except sqlite3.Error as e:
        print("Error al crear la tabla:", e)

def borrar_datos_existentes(conn):
    """
    Borra los datos existentes en la tabla de noticias.
    """
    try:
        c = conn.cursor()
        c.execute('DELETE FROM noticias')
        c.execute('DELETE FROM sqlite_sequence WHERE name="noticias"')  # Reinicia el contador de autoincremento
    except sqlite3.Error as e:
        print("Error al borrar los datos existentes:", e)

def insertar_datos(conn, titulos_y_resumenes):
    """
    Inserta nuevos datos en la tabla de noticias.
    """
    try:
        c = conn.cursor()
        datos = [(item['titulo'], item['resumen']) for item in titulos_y_resumenes]
        c.executemany('''
            INSERT INTO noticias (titulo, resumen) VALUES (?, ?)
        ''', datos)
        conn.commit()
    except sqlite3.Error as e:
        print("Error al insertar los datos:", e)

def guardar_en_base_de_datos(titulos_y_resumenes, db_name='noticias.db'):
    """
    Guarda los títulos y resúmenes en una base de datos SQLite.
    """
    conn = conectar_base_de_datos(db_name)
    if conn:
        crear_tabla_si_no_existe(conn)
        borrar_datos_existentes(conn)
        insertar_datos(conn, titulos_y_resumenes)
        conn.close()
