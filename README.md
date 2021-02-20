# Questionary
Multichoice tests in YAML format with automated conversion to JSON, DOCX, 
CSV, Moodle XML and WEB page.

Test de respuesta múltiple guardados en formato 
[YAML](https://es.wikipedia.org/wiki/YAML) con conversión automática 
desde este formato a otros útiles como son DOCX, CSV, XML de Moodle 
o formato de página WEB.


## Página web de Questionary

Creada automáticamente a partir de los cuestionarios:

https://picuino.github.io/questionary


## Estructura de directorios

### Directorio multichoice
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
Category: Electricity
Title: Código de colores 1
Author: Carlos Pardo
Show_max: 20

---

```

**Category**:  es la categoría de las preguntas. Siempre se escribe en inglés 
para que todos los bloques de preguntas tengan la misma categoría 
independientemente de su idioma.

**Title**: es el título del fichero de preguntas. Debe ser único y no repetirse 
entre ficheros.

**Author**: autor o autores (se escribirían con comas entre ellos) del fichero
 de preguntas.

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
    - 2.0Ω
    - 21Ω
    - 1.01Ω
```

**Title**: es el título de la pregunta. Si no aparece nada en este campo, 
se tomará como título el texto que aparece en el siguiente campo Question.

**Question**: es la pregunta que le aparece al estudiante

Image: la imagen con la ruta para acceder a ella. El nombre de la imagen debe
comenzar por una palabra que indique la categoría a la que pertenece.

**Image_width**: Ancho en pixels con el que se debe mostrar la imagen en pantalla.

**Choices**: listado de respuestas u opciones. La primera siempre debe ser cierta y 
las siguientes deben ser falsas. Se pueden colocar desde 2 hasta 6 respuestas 
como máximo.


### Directorio images
En este directorio se guardan todas las imágenes utilizadas en los 
cuestionarios. 

El nombre de cada imagen debe comenzar por una palabra que indique 
la categoría a la que pertenece, otra palabra con la subcategoría y una
terminación para distinguirla de otras.

Por ejemplo la imagen electric-simbolo-interruptor.png
pertenece a la categoría de electricidad, subcategoría de símbolos eléctricos 
y se trata de un interruptor.


### Directorio image/kicad e image/libreoffice
Este directorio contiene los proyectos en formato KiCAD y formato
LibreOffice necesarios para generar las imágenes del proyecto.


### Directorio image/thumbs
Este subdirectorio contiene todas las imágenes en formato pequeño (thumbnails).

Las imágenes pequeñas de este directorio se generan automáticamente a 
partir de las imágenes del directorio "images" y sirven para utilizarlas
en la documentación del proyecto.


### Directorio build
En este directorio se guardan automáticamente los formatos DOCX, CSV, y 
XML de Moodle a partir de los ficheros YAML en texto plano, cuando se 
ejecuta la macro en Pyhton questionary.py


### Directorio docs
En este directorio se genera automáticamente las páginas web de los 
cuestionarios.
Los únicos archivos que habrá que editar a mano son los ficheros de 
índice: index.html, index_en.html e index_gal.html para incluir en ellos 
las páginas que se desee en el orden y con el título correcto.


### Directorio templates
Directorio interno que contiene las plantillas necesarias para generar 
automáticamente todos los ficheros.


### Directorio venv
Directorio utilizado por Python para guardar el entorno y las
librerías de trabajo. Se puede prescindir de él si se instala Python
en el ordenador junto con todas las librerías necesarias.

