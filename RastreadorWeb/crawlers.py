import requests, colorama
from bs4 import BeautifulSoup
from colorama import Fore, Style
import sqlite3

def main():
    soup = obtencionPaginaWebWiki()
    soup2 = obtencionPaginaWebESI()
    (titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn,esi_content) = obtencionInfoYAlmacenamiento(soup,soup2)
    imprimirContenido(titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn,esi_content) 
    meterDatosBBDD(titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn,esi_content)


def obtencionPaginaWebWiki():
    
    url = 'https://en.wikipedia.org/wiki/Main_Page'                                                                     # URL de la página principal de Wikipedia en inglés
    response = requests.get(url)                                                                                        # Realizamos una solicitud GET a la página web
    soup = BeautifulSoup(response.content, 'html.parser')                                                               # Creamos el objeto BeautifulSoup y lo configuramos para parsear HTML

    return soup;

def obtencionPaginaWebESI():

    # Hacemos la petición HTTP a la página web de la ESI
    url = 'https://esi.uclm.es'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    return soup

def obtencionInfoYAlmacenamiento(soup,soup2):
    
    titulo = soup.find('title').text                                                                                    # Buscamos el título principal de la página

    bienvenida_section = soup.find('div', {'id': 'mp-welcomecount'})                                                    # Buscamos la bienvenida y la guardamos en la variable.
    bienvenida_content = bienvenida_section.text.strip()

    introduccion_element = soup.find('div', {'id': 'mw-content-text'}).find('p').text                                   # Buscamos la introducción de la página, que se encuentra en un div con id "mp-topbanner"
    if introduccion_element:
        introduccion = introduccion_element
    else:
        introduccion = None

    #Buscamos el contenido de las noticias
    noticias_section = soup.find('div', {'id': 'mp-itn'})
    noticias = noticias_section.text.strip()

    # Buscamos el contenido del apartado "did you know..."" y obtener su contenido
    did_you_know_section = soup.find('div', {'id': 'mp-dyk'})
    did_you_know_content = did_you_know_section.text.strip()

    # Buscamos el contenido del apartado "Today's featured picture" y obtener su contenido
    featured_picture_section = soup.find('div', {'id': 'mp-tfp'})
    featured_picture_content = featured_picture_section.text.strip()

    # Buscamos el contenido del apartado "On this day" y obtener su contenido
    on_this_day_section = soup.find('div', {'id': 'mp-otd'})
    on_this_day_content = on_this_day_section.text.strip()

    # Encontrar la sección "Other areas of Wikipedia" y obtener su contenido
    other_areas_section = soup.find('div', {'id': 'mp-other-content'})
    other_areas_content = other_areas_section.text.strip()

    # Encontrar la sección "Wikipedia's sister projects" y obtener su contenido
    wiki_projects_section = soup.find('div', {'id': 'mp-sister-content'})
    wiki_projects_content = wiki_projects_section.text.strip()

    # Encontrar la sección "Wikipedia languages" y obtener su contenido
    wiki_languages_section = soup.find('div', {'class': 'wikipedia-languages nourlexpansion'})
    wiki_languages_content = wiki_languages_section.text.strip()


    # Para la foto destacada de hoy y demas fotos de los otros apartados:"
  
    links = soup.find_all('img')                                                                                          #Primero recogemos todas las fotos de la pagina web.
    contador = 0
    for imagen in links:
        img = imagen.get('src')
        contador += 1
        # print(img)    para imprimir todas las url de las imagenes de la pawina web.
        if contador == 8:
            imagen_destacada = img;
        if contador == 5:
            imagen_dyk = img;
        if contador == 7:
            imagen_otd = img;
        if contador == 4:
            imagen_ftfa = img;
        if contador == 6:
            imagen_itn = img;
    
    #PARA OBTENER LA INFORMACION DE LA PAGINA WEB DE LA ESI:
    #----------------------------------------------------------------------------------------

    titulo2 = soup2.find('title').text       

    esi_section = soup2.find('div', {'class': 'mkd-wrapper'})
    esi_content = esi_section.text.strip()

    return (titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn,esi_content)

def meterDatosBBDD(titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn,esi_content):
    # Crear una conexión a la base de datos
    conn = sqlite3.connect('BBDDcrawler.db')

    # Crear un cursor para la base de datos
    c = conn.cursor()

    """
    # Crear una tabla para almacenar los datos
    c.execute('''CREATE TABLE datos (titulo text, bienvenida_content text,introduccion,noticias text,did_you_know_content text,featured_picture_content text,on_this_day_content text,other_areas_content text,wiki_projects_content text,wiki_languages_content text, imagen_destacada text,imagen_dyk text,imagen_otd text,imagen_ftfa text,imagen_itn text,esi_content text)''')
    """


    # Insertar datos en la tabla
    c.execute("INSERT INTO datos VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn,esi_content))

    # Guardar los cambios en la base de datos
    conn.commit()

    # Ejecutar la consulta
    c.execute('SELECT titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn, esi_content FROM datos')

    # Recuperar los datos
    datos = c.fetchall()
    for fila in datos:
        print(fila)

    c.execute("DELETE FROM datos")
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

def imprimirContenido(titulo, bienvenida_content,introduccion,noticias,did_you_know_content,featured_picture_content,on_this_day_content,other_areas_content,wiki_projects_content,wiki_languages_content, imagen_destacada,imagen_dyk,imagen_otd,imagen_ftfa,imagen_itn, esi_contet):
    
    # Imprimimos los resultados
    print(Fore.MAGENTA+'Título:\n'+Style.RESET_ALL, titulo)
    print(Fore.MAGENTA+'\nBienvenida:\n'+Style.RESET_ALL, bienvenida_content)
    print(Fore.MAGENTA+"\nFrom today's featured article:"+Style.RESET_ALL+"\nURL imagen: "+Fore.GREEN+imagen_ftfa+ Style.RESET_ALL+'\n', introduccion)
    print(Fore.MAGENTA+'\nIn the news:'+Style.RESET_ALL+'\nURL imagen: '+Fore.GREEN+imagen_itn+Style.RESET_ALL,noticias)

    print(Fore.MAGENTA+"\nDid you know ...:"+Style.RESET_ALL+"\nURL imagen: "+Fore.GREEN+imagen_dyk+Style.RESET_ALL+'\nNombre de la imagen: ', did_you_know_content)
    print(Fore.MAGENTA+"\nOn this day:"+Style.RESET_ALL+"\nURL imagen: "+Fore.GREEN+imagen_otd+Style.RESET_ALL+'\n', on_this_day_content)

    print(Fore.MAGENTA+"\nToday's featured picture:"+Style.RESET_ALL)
    if imagen_destacada is not None:
        print('URL: '+Fore.GREEN+imagen_destacada+Style.RESET_ALL)
        print('\n'+featured_picture_content)
    else:
        print('No se encontró ninguna imagen destacada')

    print(Fore.MAGENTA+"\nOther areas of Wikipedia:\n"+Style.RESET_ALL, other_areas_content)

    print(Fore.MAGENTA+"\nWikipedia's sister projects:\n"+Style.RESET_ALL, wiki_projects_content)

    print(Fore.MAGENTA+"\nWikipedia languages:\n"+Style.RESET_ALL, wiki_languages_content)

    print(Fore.MAGENTA+"\n\nCONTENIDO PAGINA WEB ESI:\n--------------------------------\n"+Style.RESET_ALL, esi_contet)

    colorama.deinit()


if __name__ =='__main__':
    main()    
