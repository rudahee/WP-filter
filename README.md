# Wallapaper Filter

----

## Este programa es una pequeña prueba para aprender a usar scripts con argumentos.

Este programa recorre recursivamente una serie de carpetas donde busca archivos con una resolucion que le pasamos por parametro, yo lo uso para seleccionar imagenes con una determinada resolucion en mi sistema.

----

### ARGUMENTOS DEL SCRIPTS

`main.py [-h] -i path -o path -x 1234 -y 1234 -t 0`

* -h --help             Muestra la ayuda. 
* -i --input            Carpeta raiz desde la que se empezara a buscar (sin el **'/'** final)
* -o --output           Carpeta donde se copiaran las imagenes coincidentes (sin el **'/'** final)
* -x --xaxis            Ancho de la imagen
* -y --yaxis            Alto de la imagen
* -t --time             tiempo entre imagenes [0 = Sin espera] (Conveniente para imagenes MUY grandes)

