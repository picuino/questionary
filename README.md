Questionary
===========

Test de respuesta múltiple guardados en formato 
[YAML](https://es.wikipedia.org/wiki/YAML) con conversión automática 
desde este formato a otros útiles como son DOCX, CSV, XML de Moodle 
o formato de página WEB.


Página web de questionary
=========================
Creada automáticamente a partir de los cuestionarios.

Test alojados en picuino.com:

   https://www.picuino.com/test


Test alojados en GitHub:
   
   https://picuino.github.io/questionary/index.html


Créditos y licencias
====================

https://github.com/picuino/questionary/blob/master/Licenses.md


Estructura de directorios
=========================

## Directorio multichoice
En este directorio se guardan los archivos con todas las preguntas y las 
múltiples respuestas a cada pregunta. Es el directorio con el que se debe
trabajar si se quiere aportar preguntas o leerlas y es la fuente a partir
de la que se generan automáticamente todos los demás ficheros del proyecto.

El formato utilizado es el de fichero de texto
[YAML](https://es.wikipedia.org/wiki/YAML) guardado con formato UTF-8 
para gestionar los caracteres especiales tales como acentos.

Este formato YAML se puede editar fácilmente con un simple block de notas.

**El primer elemento del fichero YAML** será una cabecera con los 
siguientes campos:

```
Category: Materiales
Title: La madera
Copyright: 2021 por Carlos Pardo
License: Creative Commons Attribution-ShareAlike 4.0
Show_max: 20

---

```

**Category**:  es la categoría de las preguntas. La categoría es por ejemplo
  materiales, electricidad, mecánica, programación, dibujo, etc.
  La categoría es común y se repetirá en varios ficheros que traten 
  sobre el mismo tema.

**Title**: es el título del fichero de preguntas. Debe ser único y no repetirse 
  entre ficheros. No debe repetir el texto ya escrito en la categoría.
  Ejemplos de títulos para la categoría de Materiales serían 'La madera' o
  'Los metales'

**Copyright**: fecha de creación y nombre del autor o autores del fichero 
  de preguntas. En el caso de que haya más de un autor, se separan los 
  nombres por comas. La coma solo debe utilizarse para separar autores entre
  sí.

**License**: Licencia con la que se publica el contenido del archivo.

**Show_max**: número máximo de preguntas que se mostrarán en la página web. 
  Es útil para que los ficheros que tienen muchas preguntas repetitivas solo 
  muestren un subconjunto al azar de todas ellas.
  En caso de que valga cero, se mostrarán todas las preguntas del cuestionario.


**Los siguientes elementos del fichero YAML** serán cada una de las 
preguntas y sus respuestas:

```
---

- Title: Código de colores 1.0 Ohmios
  Question: ¿Qué valor tiene esta resistencia?
  Image: images/electric-resistencia-1_0.png
  Image_width: 320
  Choices:
    - 1.0Ω
    - 10Ω
    - 1.0kΩ
    - 101Ω
```

**Title**: es el título de la pregunta. Si no aparece nada en este campo, 
se tomará como título el texto que aparece en el siguiente campo Question.

**Question**: es la pregunta que le aparece al estudiante

**Image**: imagen con la ruta para acceder a ella. El nombre de la imagen debe
comenzar por una palabra que indique la categoría a la que pertenece.

**Image_width**: ancho en pixels con el que se debe mostrar la imagen en pantalla.

**Choices**: listado de respuestas u opciones. La primera siempre debe ser cierta y 
las siguientes deben ser falsas. Se pueden escribir desde 2 hasta 6 respuestas 
como máximo.

**Número de preguntas por fichero**:

Los ficheros deben tener aproximadamente unas 30 preguntas y tratar de un mismo
tema específico.

Un numero mayor de preguntas hace que sean difíciles de responder en poco 
tiempo y que los ficheros de preguntas sean difíciles de manejar para los
profesores.
Un número menor de 30 preguntas hace que estas se respondan muy rápido y 
que las preguntas estén demasiado divididas en muchos subtemas o 
que haya pocas preguntas para evaluar cada tema.

Los alumnos tardan de 15 a 25 minutos en terminar un test de
30 preguntas, repitiéndolas si es necesario para obtener buena nota.


## Directorio multichoice/build
En este directorio se guardan automáticamente los formatos DOCX, CSV, y 
XML de Moodle a partir de los ficheros YAML en texto plano, cuando se 
ejecuta la macro en Pyhton _multichoice.py


## Directorio multichoice/templates
Directorio interno que contiene las plantillas necesarias para generar 
automáticamente todos los ficheros.


## Directorio docs
En este directorio se generan automáticamente las páginas web de los 
cuestionarios.
Los únicos archivos que habrá que editar a mano son los ficheros de 
índice: index.html, index_en.html e index_gal.html para incluir en ellos 
las páginas que se desee en el orden y con el título correcto.


## Directorio images
En este directorio se guardan todas las imágenes utilizadas en los 
cuestionarios. 

El nombre de cada imagen debe comenzar por una palabra que indique 
la categoría a la que pertenece, otra palabra con la subcategoría y una
terminación para distinguirla de otras.

Por ejemplo la imagen electric-simbolo-interruptor.png
pertenece a la categoría de electricidad, subcategoría de símbolos eléctricos 
y se trata de un interruptor.


## Directorio images/kicad e images/libreoffice
Este directorio contiene los proyectos en formato KiCAD y formato
LibreOffice necesarios para generar las imágenes del proyecto.


## Directorio images/thumbs
Este subdirectorio contiene todas las imágenes en formato pequeño (thumbnails).

Las imágenes pequeñas de este directorio se generan automáticamente a 
partir de las imágenes del directorio "images" y sirven para utilizarlas
en la documentación del proyecto.


## Directorio venv
Directorio utilizado por Python para guardar el entorno y las
librerías de trabajo. Se puede prescindir de él si se instala Python
en el ordenador junto con todas las librerías necesarias.


Instalación en Windows
======================

## INTERPRETE PYTHON
Para ejecutar las macros de Python necesarias para renderizar
todos los archivos, será necesario instalar el 
[intérprete Python](https://www.python.org/downloads/windows/)
La última versión en el momento de escribir estas líneas es la 3.9
pero la macro funciona también con versiones 3.x antiguas.

Durante la instalación será recomendable cambiar el directorio de 
instalación a /Bin/Python39.
En el caso de no hacerlo así, es necesario cambiar la dirección del 
intérprete Python que se encuentra en el archivo _gnu-bash.bat
por la verdadera ruta en la que Python esté instalado.


## LIBRERIAS DE PYTHON
Además de instalar el intérprete, será necesario instalar las librerías
necesarias para trabajar con archivos YAML, con templates Jinja y con
imágenes.

En un directorio de Python se deben ejecutar las siguientes órdenes
por ejemplo en un archivo .bat o en la línea de comandos:

~~~
@set PATH=C:/Bin/Python39;%PATH%
python -m pip install --upgrade Jinja2
python -m pip install --upgrade PyYAML
python -m pip install --upgrade Pillow
python -m pip install --upgrade python-docx
~~~

Cambiando C:/Bin/Python39 por la verdadera ruta en la que se encuentre
el intérprete de Python.


## ARCHIVOS MAKEFILE
Mediante estos archivos es posible automatizar otras tareas tales como
generar imágenes a partir de archivos .pdf o generar thumbnails (pequeñas
imágenes) a partir de las imágenes grandes.

No es necesario instalar el soporte para archivos makefile, pero si muy
recomendable si se quiere aprovechar la generación automática de imágenes.

**Cygwin**

El primer paquete que habrá que instalar será [Cygwin](https://cygwin.com/install.html)
que es una colección de herramientas Open Source que proveen una funcionalidad
similar a una distribución Linux en Windows. Este paquete proporciona las 
utilidades make y bash.

Es recomendable instalar Cygwin en el directorio /Bin/cygwin64 o cambiar
en el archivo _gnu-bash.bat la ruta donde se haya instalado

**ImageMagick**

El siguiente paquete a instalar será [imagemagick](https://imagemagick.org/script/download.php#windows)
que es un conjunto de utilidades Open Source en linea de comandos utilizadas
para automatizar las tareas de manejo de imágenes tales como recortar, posterizar,
añadir transparencias, convertir entre formatos de imagen, generar thumbnails, etc.

Es recomendable instalar ImageMagick en el directorio /Bin/imagemagick o cambiar 
en el archivo _gnu-bash.bat la ruta donde se haya instalado.


**Optipng**

Esta es una utilidad Open Source que recomprime las imágenes PNG para que ocupen
menos espacio y estén libres de errores de integridad.
Se puede descargar desde su página de sourceforge: http://optipng.sourceforge.net/
y es recomendable instalarlo en /Bin/imagetools o cambiar
en el archivo _gnu-bash.bat la ruta donde se haya instalado.

Existen otras utilidades Open Source  para línea de comandos que optimizan 
imágenes PNG tal como [png optimizer CL](http://psydk.org/pngoptimizer), 
pero en caso de instalar otra utilidad será necesario cambiar la cabecera 
de los archivos makefile.


**XPDF**

Esta utilidad Open Source se utiliza en el proyecto para convertir archivos
desde el formato PDF al formato de imagen PNG.
Se pueden instalar las utilidades para linea de comandos desde esta 
dirección: https://www.xpdfreader.com/download.html

Es recomendable instalar XPDF en el directorio /Bin/xpdf o cambiar 
en el archivo _gnu-bash.bat la ruta donde se haya instalado.
