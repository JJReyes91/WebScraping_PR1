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

De todo el repositorio de datos que contiene la web, únicamente se realizará la captura de los periodos **2018** y **2019** en su totalidad de atributos (**Fecha, Super 95, Super 95 (Sin imp.), Diesel, Diesel (Sin imp.), Diesel Cal., Diesel Cal. (Sin imp.)**) y registros.  

Estos datos capturados permetirán conocer el evolutivo de los derivados del petroleo (valor con y sin impuestos) en España y a su vez poder conocer la tendencia general que tienen.

## Captura de datos  
