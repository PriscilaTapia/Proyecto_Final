import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

#marcado de página

url = requests.get("https://www.bbc.com/mundo/topics/cpzd498zkxgt")
content = url.content
statusCode = url.status_code
if statusCode == 200:
    site = BeautifulSoup(content, 'html.parser') #parse (analizador)

    #bloque donde se encuantra cada noticia
    noticias = site.findAll('article', class_ = 'qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left') 

        #iteración para obtener los datos que queremos extraer 
    for noticia in noticias:
        titulo = noticia.find('a', class_ =  'qa-heading-link lx-stream-post__header-link').text
        cuerpo_noticia = noticia.find('div', class_ = 'lx-stream-related-story').text
        link = noticia.find('div', class_='gel-3/8@l').a.get('href')
        lista_noticias.append([titulo.strip(),cuerpo_noticia,link])
    
    #Generar dataframe
    news = pd.DataFrame(lista_noticias, columns=['Titulo','Cuerpo','Link'])
else:
    print ("Error en la pagina")
#exportamos dataframe
#news.to_csv('noticias.csv', index=False)
#print(lista_noticias)