import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Obtiene la ruta del directorio actual donde está scrapy2.py
current_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_dir, 'chromedriver_win32', 'chromedriver.exe')

def obtener_titulos_y_links(url):
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Ejecuta el navegador en modo headless (sin ventana)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(3)  # Espera para asegurar que el contenido dinámico se cargue completamente

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Encuentra los primeros 10 elementos que contienen los títulos y enlaces
    noticias = soup.find_all('h2', limit=10)
    titulos_y_links = []
    for noticia in noticias:
        titulo = noticia.get_text(strip=True)
        enlace_tag = noticia.find('a', href=True)
        if enlace_tag:
            enlace = enlace_tag['href']
            if not enlace.startswith('http'):
                enlace = 'https://elcomercio.pe' + enlace
        else:
            enlace = None
        titulos_y_links.append({'titulo': titulo, 'enlace': enlace})
    return titulos_y_links

def obtener_resumen(url):
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)
    time.sleep(3)  # Espera para asegurar que el contenido dinámico se cargue completamente
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Intenta encontrar el resumen en el h2 o meta tag como en el ejemplo anterior
    resumen_tag = soup.find('h2', {'itemprop': 'name', 'class': 'sht__summary sht--w-list'})
    if resumen_tag:
        resumen = resumen_tag.get_text(strip=True)
    else:
        meta_tag = soup.find('meta', attrs={'name': 'DC.description', 'lang': 'es'})
        resumen = meta_tag['content'].strip() if meta_tag and 'content' in meta_tag.attrs else 'Resumen no disponible'
    
    return resumen

# URL de la página
url = 'https://elcomercio.pe/ultimas-noticias/'
titulos_y_links = obtener_titulos_y_links(url)

# Ahora obtenemos los resúmenes
titulos_y_resumenes = []
for item in titulos_y_links:
    titulo = item['titulo']
    enlace = item['enlace']
    if enlace:
        resumen = obtener_resumen(enlace)
    else:
        resumen = 'Sin resumen'
    titulos_y_resumenes.append({'titulo': titulo, 'resumen': resumen})

# Imprime los títulos y resúmenes
for i, item in enumerate(titulos_y_resumenes, start=1):
    print(f"Título {i}: {item['titulo']}")
    print(f"Resumen {i}: {item['resumen']}")
    print('-----------------------------')
