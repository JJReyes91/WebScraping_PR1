# Importación de las librerias
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

#Inicialización de las variables
Fechas=[]
Supers=[]
Supersins=[]
Diesels=[]
Dieselsins=[]
DieselCals=[]
DieselCalsins=[]
datos=[]

año = ['2018','2019']
for a in año:
	#Indicar la ruta
	url_page = 'https://datosmacro.expansion.com/energia/precios-gasolina-diesel-calefaccion/espana?anio=' + a

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
		Supers.append(float(valor.replace(',','.')))
		
		valor=datos[2].replace('€',"")
		Supersins.append(float(valor.replace(',','.')))
		
		valor=datos[3].replace('€',"")
		Diesels.append(float(valor.replace(',','.')))
		
		valor=datos[4].replace('€',"")
		Dieselsins.append(float(valor.replace(',','.')))
		
		valor=datos[5].replace('€',"")
		DieselCals.append(float(valor.replace(',','.')))	
		
		valor=datos[6].replace('€',"")
		DieselCalsins.append(float(valor.replace(',','.')))

		#Limpiamos el contenido de la variable datos para almacenar el siguiente registro
		datos.clear()

#Gráfico precio combustibles al consumidor

plt.plot(Fechas, Supers, color='blue')
plt.plot(Fechas, Diesels, color='red')
plt.plot(Fechas, DieselCals, color='orange')
plt.xlabel ('Fecha')
plt.ylabel('Precio [€]')
plt.legend(['Super 95','Diesel','Diesel Calefacción'],loc='upper center')
plt.title('Precios productos petroliferos en España (consumidor)')
plt.savefig('con impuestos')

"""
#Gráfico precio combustibles sin impuesto

plt.plot(Fechas, Supersins, color='blue')
plt.plot(Fechas, Dieselsins, color='red')
plt.plot(Fechas, DieselCalsins, color='orange')
plt.xlabel ('Fecha')
plt.ylabel('Precio [€]')
plt.legend(['Super 95','Diesel','Diesel Calefacción'],loc='upper center')
plt.title('Precios productos petroliferos en España (sin impuestos)')
plt.savefig('sin impuestos')
"""

#Generación de la tabla resultante. Importamos la librería panda
BBDD = pd.DataFrame({'Fecha': Fechas,
                       'Super 95': Supers,
                       'Super 95 Sin imp.': Supersins,
                       'Diesel': Diesels,
                       'Diesel Sin imp.': Dieselsins,
                       'Diesel Cal.': DieselCals,
                       'Diesel Cal. Sin imp.': DieselCalsins,})

BBDD.to_csv('outup.csv')