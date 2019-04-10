# Importación de las librerias
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from fake_useragent import UserAgent
from fake_useragent import UserAgent
import requests

#Inicialización de las variables
Fechas=[]
Supers=[]
Supersins=[]
Diesels=[]
Dieselsins=[]
DieselCals=[]
DieselCalsins=[]
datos=[]

#Lectura del robots.txt
response = get('https://datosmacro.expansion.com/robots.txt')
test = response.text
print('robots.txt para la web https://datosmacro.expansion.com/')
print('========================================================')
print(test)

#Modificar user-agent

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
url = 'https://datosmacro.expansion.com'
htmlContent = get(url, headers=header)

#Inicio del bucle para la captura de datos

año = ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
for a in año:
	#Indicar la ruta
	url_page = 'https://datosmacro.expansion.com/energia/precios-gasolina-diesel-calefaccion/espana?anio=' + a

	#Verificación que la página existe
	try:
	    html = urlopen(url_page)
	except HTTPError as e:
		sys.exit('HTTP error')
	except URLError as e:
		sys.exit('Server not found!')
	else:
		pass

	#Realizar petición (target) de la pagina web
	respuesta = get(url_page).text

	#Procesado del HTML mediante el analizador lxml
	procesado = BeautifulSoup(respuesta, 'lxml')

	#Selección de la tablata. Busca la marca <tbody> que en este caso únicamente hay 1
	tabla = procesado.find('tbody')

	#Generación del bucle para cada uno de los registros <tr>
	for registro in tabla.find_all('tr'):
		for celda in registro.find_all('td'):
			dato=celda.text
			datos.append(dato)

		Fechas.append(datetime.strptime(datos[0],'%d/%m/%Y'))
		
		valor=datos[1].replace('€',"")
		Supers.append(round(float(valor.replace(',','.')),2))
		
		valor=datos[2].replace('€',"")
		Supersins.append(round(float(valor.replace(',','.')),2))
		
		valor=datos[3].replace('€',"")
		Diesels.append(round(float(valor.replace(',','.')),2))
		
		valor=datos[4].replace('€',"")
		Dieselsins.append(round(float(valor.replace(',','.')),2))
		
		valor=datos[5].replace('€',"")
		DieselCals.append(round(float(valor.replace(',','.')),2))	
		
		valor=datos[6].replace('€',"")
		DieselCalsins.append(round(float(valor.replace(',','.')),2))

		#Limpiamos el contenido de la variable datos para almacenar el siguiente registro
		datos.clear()

#Generación de la tabla resultante. Importamos la librería panda
BBDD = pd.DataFrame({'Fecha': Fechas,
                       'Super 95': Supers,
                       'Super 95 Sin imp.': Supersins,
                       'Diesel': Diesels,
                       'Diesel Sin imp.': Dieselsins,
                       'Diesel Cal.': DieselCals,
                       'Diesel Cal. Sin imp.': DieselCalsins,})

#Se añade el campo año al dataframe donde se recoge únicamente el año del campo fecha
BBDD['Año'] = BBDD['Fecha'].dt.year
BBDD.index = BBDD['Fecha']

#Se genera el archivo csv con los datos descargados mediante el webscraping
BBDD.to_csv('output.csv',index=False)

#Se genera un nuvo dataframe con los valores promedios por año de los distintos combustibles.
BBDD2 = BBDD.resample('Y').mean().round(2)

"""
#Gráfico precio combustibles sin impuesto
ax = plt.gca()
BBDD2.plot(kind='line', x='Año', y='Super 95 Sin imp.',color='blue',ax=ax)
BBDD2.plot(kind='line', x='Año', y='Diesel Sin imp.',color='red',ax=ax)
BBDD2.plot(kind='line', x='Año', y='Diesel Cal. Sin imp.',color='orange',ax=ax)
plt.title('Precio promedio por año derivados petroliferos en España')
plt.ylabel('Precio [€]')

#Se genera la imagen del grafico generado
plt.savefig('Gráfico resultado II')
"""

#Gráfico precio combustibles al consumidor
ax = plt.gca()
BBDD2.plot(kind='line', x='Año', y='Super 95',color='blue',ax=ax)
BBDD2.plot(kind='line', x='Año', y='Diesel',color='red',ax=ax)
BBDD2.plot(kind='line', x='Año', y='Diesel Cal.',color='orange',ax=ax)
plt.title('Precio promedio por año derivados petroliferos en España')
plt.ylabel('Precio [€]')

#Se genera la imagen del grafico generado
plt.savefig('Gráfico resultado')

"""
#Generar archivo con los valores promedios por año.
BBDD2.to_csv('outputII.csv')
"""