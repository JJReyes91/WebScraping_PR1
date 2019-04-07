# PRÁCTICA 1: WEB SCRAPING PRECIOS DE LOS DERIVADORS DEL PETRÓLEO EN ESPAÑA 
Asígnatura: Tipología y ciclo de vida de los datos.  
Máster: Data Science (UOC)  
Alumno: Javier Jiménez Reyes  

## Introducción  
Es una realizadad el echo que el precio de los combustibles van variando con el tiempo a medida que el mercado los va regulando. De este modo estos suben y bajan a medida en función de varios condicionantes. Pero ¿cúal es la tendencia general que están siguiendo?  
El objetivo que se persigue en esta práctica consistirá en capturar mediante la técnica del web scraping, datos que permitan dar respuesta a la pregunta formulada.  

## Origen web, datos y características  
El sitio web [Datosmacro.com](https://datosmacro.expansion.com/) cuenta con un amplio repositorio de datos de distinta temática. Entre todos ellos se puede encontrar el evolutivo de los [Precios de los derivados del petroleo en España](https://datosmacro.expansion.com/energia/precios-gasolina-diesel-calefaccion/espana).  
En este repositorio se indica la evolución del previo del **Super95**, **Diesel** y **Diesel para calefacción** con y sin impuestos añadidos a su valor. 

De todo el repositorio de datos que contiene la web, únicamente se realizará la captura de los periodos **2018** y **2019** en su totalidad de atributos (**Fecha, Super 95, Super 95 (Sin imp.), Diesel, Diesel (Sin imp.), Diesel Cal., Diesel Cal. (Sin imp.)**) y registros, siendo el primero de ellos la fecha de medida del valor en € del resto.   

De los datos capturados se graficarán únicamente los valores con impuesto que son los que muestran el valor de caras al consumidor final. Estos datos permitirán conocer el evolutivo del valor de los derivados del petroleo en España y a su vez poder conocer la tendencia general que tienen.

## Captura de datos 
Para la captura de datos mediante la técnica de webscraping se a utilizado el lenguaje de programación **Python**. Para la ejecución del *script* es necesario la instalación del sistema de gestión de paquetes **_PIP_** para Python, así como las siguientes bibliotecas:  
```
pip install requests        # Biblioteca para realizar la patición (target) a la página web y facilita la interacción con esta.
pip install beautifulsoup4  # Biblioteca para realizar análisis de documentos HTML.
pip install lxml            # Biblioteca para realizar el procesado del HTML a lxml.
pip install DateTime        # Biblioteca para la conversión de la varable string a date.
pip install matplotlib      # Biblioteca para realizar gráficos
pip install pandas          # Biblioteca para la generación de DataFrames(hojas de datos) que permitan exportar a csv.
```
Los aspectos que se han tenido en cuenta para la captura de los datos han sido:

1. Las marcas utilizadas: 
   -  \<tbody>\: Marca donde se encuentra la tabla con los datos.
   -  \<tr>\: Marca los distitntos registros.
   -  \<td>\: Marca las distintas celdas del registro.
2. Se deberá convertir la variable **Fecha** del tipo **_string_** a tipo **_date_**.
3. Se debará eliminar el carácter **€** de los atributos correspondiente al valor de los distintos combustibles. 
4. Se deberá convertir el carácter **,** a **.** de los valores de los distintos combustibles, para posteriormente poder convertir el      tipo de variable de **_string_** a **_float_**.

Los resultados se almacenarán en un archivo **.csv** con el nombre **output.csv**.  

## Resultados

El siguiente gráfico representa los datos capturados en el periodo 2018 y 2019 referente a la evolución del valor (con impuestos) de los distintos derivados del petroleo. Tal como se puede observar, el gráfico muestra que la tendencia del velor de todos lo combustibles es al alza a excepción de los altibajos (fluctuación) que tienen a lo largo del periodo estudiado.

![Image description](https://github.com/JJReyes91/WebScraping_PR1/blob/master/con%20impuestos.png)
