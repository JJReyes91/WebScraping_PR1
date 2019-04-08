# PRÁCTICA 1: WEB SCRAPING PRECIOS DE LOS DERIVADORS DEL PETRÓLEO EN ESPAÑA 
Asígnatura: Tipología y ciclo de vida de los datos.  
Máster: Data Science (UOC)  
Alumno: Javier Jiménez Reyes  

## Introducción  
Es una realidad el hecho que el precio de los combustibles va variando con el tiempo a medida que el mercado los va regulando. De este modo estos suben y bajan en función de varios condicionantes, pero ¿cuál ha sido su evolución?  
El objetivo que se persigue en esta práctica consiste en capturar mediante la técnica del **_webscraping_**, datos que permitan dar respuesta a la pregunta formulada.

## Contexto
El sitio web [Datosmacro.com](https://datosmacro.expansion.com/) cuenta con un amplio repositorio de datos de distinta temática, los cuales actualiza en base a un seguido de [webs externas](https://datosmacro.expansion.com/legal/fuentes) que utiliza como **fuentes de información primarias**. 

Entre todos estos repositorios se encuentra el evolutivo de los [Precios de los derivados del petróleo en España](https://datosmacro.expansion.com/energia/precios-gasolina-diesel-calefaccion/espana). En este se indica la evolución del precio de los distintos combustibles fósiles **Super95**, **Diesel** y **Diesel para calefacción** con y sin impuestos añadidos a su valor, dentro del contexto del consumidor final.

## Datos y características
En el desarrollo de la práctica se realizará la captura de la toralidad de los atributos (**Fecha, Super 95, Super 95 (Sin imp.), Diesel, Diesel (Sin imp.), Diesel Cal., Diesel Cal. (Sin imp.)**), cuyo valor se expresa en **€**, para todas las fechas de la web en las que constan registros (**2005** al **2019**).

Posteriormente a su captura, los datos serán agrupados por años indicando por cada uno de los combustibles el valor promedio calculado para ese período. 

Tras la agrupación por años se graficarán únicamente **los valores con impuestos** que son los que muestran el valor de caras al consumidor final. Estos datos permitirán conocer el evolutivo del valor de los derivados del petróleo en España y a su vez poder observar cual a sido su tendencia a lo largo de los últimos años.

## Captura de datos 
Para la captura de datos mediante la técnica de **_webscraping_** se a utilizado el lenguaje de programación **Python**. Para la ejecución del *script* **_Code.py_**, es necesario la instalación del sistema de gestión de paquetes **_PIP_** para Python, así como las siguientes bibliotecas:  
```
pip install requests        # Biblioteca para realizar la patición (target) a la página web y facilita la interacción con esta.
pip install beautifulsoup4  # Biblioteca para realizar análisis de documentos HTML.
pip install lxml            # Biblioteca para realizar el procesado del HTML a lxml.
pip install DateTime        # Biblioteca para la conversión de la varable string a date.
pip install matplotlib      # Biblioteca para realizar gráficos
pip install pandas          # Biblioteca para la generación de DataFrames (hojas de datos) que permitan exportar a csv.
```
Los aspectos que se han tenido en cuenta para la captura de los datos han sido:

1. Las marcas utilizadas: 
   -  \<tbody>\: Marca donde se encuentra la tabla con los datos.
   -  \<tr>\: Marca los distintos registros.
   -  \<td>\: Marca las distintas celdas del registro.
2. Se deberá convertir la variable **Fecha** del tipo **_string_** a tipo **_date_**.
3. Se deberá eliminar el carácter **€** de los atributos correspondiente al valor de los distintos combustibles. 
4. Se deberá convertir el carácter **','** a **'.'** de los valores de los distintos combustibles, para posteriormente poder convertir      el tipo de variable de **_string_** a **_float_**.

Los resultados se almacenan en un archivo **.csv** con el nombre **output.csv**.
Indicar que en el código se dejan comentados:
- La opción de graficar los valores de los carburantes sin impuestos.
- Generar un archivo outputII.csv con los registros agrupados por año (son los valores que se utilizan para realizar el gráfico). 

## Dataset output.csv
El *dataset* generado se compone de **7 atributos** y un total de **706 registros** estructurados del siguiente modo:

| Fecha    | Super 95  | Super 95 (Sin imp.) | Diesel      | Diesel (Sin imp.) | Diesel Cal. |  Diesel Cal. (Sin imp.)| Año     |
| -------- | --------- | ------------------- | ----------- | ----------------- | ----------- | ---------------------- | ------- |

La información que guardan los distintos atributos es:

- **Fecha**: Fecha del registro en formato (dd/mm/yyyy). Variable tipo **Date**.
- **Super95**: Coste del combustible Super95. Variable tipo **Float**.
- **Super95 (Sin imp.)**: Coste del combustible Super95 sin impuestos. Variable tipo **Float**.
- **Diesel**: Coste del combustible Diesel. Variable tipo **Float**.
- **Diesel (Sin imp.)**: Coste del combustible Diesel sin impuestos. Variable tipo **Float**.
- **Diesel Cal.**: Coste del combustible Diesel calefacción. Variable tipo **Float**.
- **Diesel Cal. (Sin imp.)**:Coste del combustible Diesel calefacción sin impuestos. Variable tipo **Float**.
- **Año**: Año extraído del atributo **Fecha**.

## Resultados
El siguiente gráfico representa para los años **2005** a **2019** la evolución del valor (con impuestos) promedio por año, de los distintos derivados del petróleo. 

![Image description](https://github.com/JJReyes91/WebScraping_PR1/blob/master/Gr%C3%A1fico%20resultado.png)

Algunos de los aspectos que se pueden comentar de la representación gráfica de los valores son: 
- Se aprecia una tendencia ascendente general para cada uno de los combustibles a lo largo de los años.
- La tónica general que se manteiene a lo largo de los años es que el valor del Super 95 es superior al Diesel. 
- Se aprecia un cambio de tendencia en la tónica general en el 2008, año en que el valor promedio del Diesel es superior al del Super95.   Esta punta corresponde a la subida del 4 de agosto de dicho año en el que el Diesel superó por primera vez el precio de la gasolina.
- Los máximos históricos se dan en los periodos del 2012 al 2014. 

## Agradecimientos
Agradecer al sitio web [Datosmacro.com](https://datosmacro.expansion.com/) así como el directorio de [webs externas](https://datosmacro.expansion.com/legal/fuentes) que utiliza para mantener los datos acutalizados, el haber facilitado dicha información para la realización de la práctica. 

## Licencia
El código y los datos se publicarían bajo una licencia CC BY-NC-SA 4.0, es decir, licencia **_Creative Commons Non-Commercial y Share-Alike_**. Bajo esta licencia tenemos las siguientes condiciones:
1. El material se puede copiar, redistribuir, adaptar y modificar en cualquier medio o formato, fomentando la colaboración y la filosofía open-source.
2. Se incluye el término de la atribución, para que al replicar o usar el contenido se deba citar a la fuente original.
3. El término Share Alike de la licencia nos garantiza que cualquier modificación o uso
de este material se publique bajo la misma licencia, en aras de promover la colaboración.
4. El término Non Commercial determina que el material no puede ser usado para fines comerciales y por tanto su ámbito se reduce puramente al académico.

## Recursos
Los recursos utilizados para el desarrollo de la práctica han sido: 
- *Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.*
- *Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.*
