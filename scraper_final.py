import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

#marcado de página
response = requests.get("https://cnnespanol.cnn.com/category/alimentos/")
content = response.content
site = BeautifulSoup(content, 'html.parser') #parse (analizador)

#bloque donde se encuantra cada noticia
noticias = site.findAll('article', class_ = 'news') 

#iteración para obtener los datos que queremos extraer 
for noticia in noticias:
    titulo = noticia.find('h2', class_ =  'news__title').text
    link = noticia.find('h2', class_='news__title').a.get('href')
    lista_noticias.append([titulo.strip(),link])
    lista_noticias

#Generar dataframe
news = pd.DataFrame(lista_noticias, columns=['Título', 'Link'])

#exportamos dataframe
news.to_csv('noticias.csv', index=False)
