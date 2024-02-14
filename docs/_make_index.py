#
#  Index maker (c) 2022 Carlos Félix Pardo Martín
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
import codecs
from jinja2 import Template


index_data = [
   {
      "header" : ["materiales", "Materiales"],
      "links": [
          ["es-material-classification.html", "Clasificación de los materiales"],
          ["es-material-properties-1.html", "Propiedades de los materiales I"],
          ["es-material-properties-2.html", "Propiedades de los materiales II"],
          ["es-material-properties-3.html", "Propiedades de los materiales III"],
          ["es-material-stone-1.html", "Los materiales pétreos I"],
          ["es-material-stone-2.html", "Los materiales pétreos II"],
          ["es-material-stone-3.html", "Los materiales pétreos III"],
          ["es-material-wood.html", "La madera y sus derivados"],
          ["es-material-textiles.html", "Los materiales textiles"],
          ["es-material-metals.html", "Los materiales metálicos"],
          ["es-material-plastics.html", "Los materiales plásticos"],
          ["es-material-tools-1.html", "Las herramientas I"],
          ["es-material-tools-2.html", "Las herramientas II"],
          ["es-material.html", "Materiales y Herramientas. Test global"],
      ]
   },
   {
      "header" : ["mecanica", "Mecánica"],
      "links": [
          ["es-machines-simple.html", "Máquinas simples"],
          ["es-machines-transmission1.html", "Mecanismos de<br>transmisión I"],
          ["es-machines-transmission2.html", "Mecanismos de<br>transmisión II"],
          ["es-machines-transmission3.html", "Mecanismos de<br>transmisión III"],
          ["es-machines-transformation1.html", "Mecanismos de<br>transformación I"],
          ["es-machines-transformation2.html", "Mecanismos de<br>transformación II"],
          ["es-machines.html", "Máquinas y Mecanismos. Test global"],
          ["es-mecan-poleas.html", "Cálculo de poleas y polipastos"],
          ["es-mecan-calibre-medidas.html", "Medidas con calibre"],
       ]
   },
   {
      "header" : ["neumatica", "Neumática"],
      "links": [
          ["es-neumatic-symbol-name.html", "Nombre de símbolos neumáticos (Test)"],
          ["es-neumatic-symbol-name-cloze.html", "Nombre de símbolos neumáticos (Cloze)"],
       ]
   },
   {
      "header" : ["electricidad", "Electricidad"],
      "links": [
          ["es-electric-introduction.html", "Fundamentos"],
          ["es-electric-circuits.html", "El circuito eléctrico"],

          ["es-electric-components-type.html", "Tipos de componentes"],
          ["es-electric-components-name.html", "Nombre de componentes (test)"],
          ["es-electric-components-name-cloze.html", "Nombre de componentes (cloze)"],

          ["es-electric-units-magnitudes.html", "Unidades y Magnitudes"],
          ["es-electric-ohms-law.html", "Ley de Ohm. Fundamentos"],
          ["es-electric-ohms-law-2.html", "Ley de Ohm. Cálculos"],

          ["es-electric-series-parallel-identify.html", "Identificar serie y paralelo"],
          ["es-electric-series-parallel-calc.html", "Calcular serie y paralelo"],
          ["es-electric-series-parallel-calc-2.html", "Calcular resistencia equivalente"],

          ["es-electric-resolver-circuitos-1.html", "Resolver circuitos I"],
          ["es-electric-resolver-circuitos-2.html", "Resolver circuitos II"],

          ["es-electric-energy-1.html", "Energía eléctrica I"],
          ["es-electric-energy-2.html", "Energía eléctrica II"],
          ["es-electric-energy-calc.html", "Cálculos con energía eléctrica"],

          ["es-electric-power.html", "Potencia eléctrica"],
       ]
   },
   {
      "header" : ["electronica", "Electrónica"],
      "links": [
          ["es-electric-color-code-1.html", "Código de colores 1"],
          ["es-electric-color-code-2.html", "Código de colores 2"],

          ["es-electric-breadboard.html", "Breadboard"],
          ["es-electric-digital.html", "Electrónica digital"],
       ]
   },
   {
      "header" : ["controladores", "Control Automático"],
      "links": [
          ["es-control-introduction.html", "Introducción al control automático"],
       ]
   },
   {
      "header" : ["hardware", "Hardware"],
      "links": [
          ["es-hardware-intro-1.html", "Introducción al hardware I"],
          ["es-hardware-intro-2.html", "Introducción al hardware II"],

          ["es-hardware-clasificacion-1.html", "Clasificación de los ordenadores I"],
          ["es-hardware-clasificacion-2.html", "Clasificación de los ordenadores II"],

          ["es-hardware-unidades-1.html", "Unidades de medida I"],
          ["es-hardware-unidades-2.html", "Unidades de medida II"],

          ["es-hardware-ley-moore-1.html", "Ley de Moore I"],
          ["es-hardware-ley-moore-2.html", "Ley de Moore II"],

          ["es-hardware-pc-1.html", "Hardware del ordenador personal I"],
          ["es-hardware-pc-2.html", "Hardware del ordenador personal II"],
          
          ["es-hardware-placa-base.html", "Placa base"],

          ["es-hardware-procesadores-1.html", "Procesadores I"],
          ["es-hardware-procesadores-2.html", "Procesadores II"],
          ["es-hardware-procesadores-3.html", "Procesadores III"],
          ["es-hardware-procesadores-4.html", "Procesadores IV"],

          ["es-hardware-perifericos-1.html", "Periféricos I"],
          ["es-hardware-perifericos-2.html", "Periféricos II"],
          ["es-hardware-perifericos-3.html", "Periféricos III"],
          ["es-hardware-perifericos-4.html", "Periféricos IV"],

          ["es-hardware-almacenamiento-1.html", "Almacenamiento I"],
          ["es-hardware-almacenamiento-2.html", "Almacenamiento II"],
          ["es-hardware-almacenamiento-3.html", "Almacenamiento III"],
          ["es-hardware-almacenamiento-4.html", "Almacenamiento IV"],
          ["es-hardware-almacenamiento-5.html", "Almacenamiento V"],
          ["es-hardware-almacenamiento-6.html", "Almacenamiento VI"],

          ["es-hardware-comunicaciones-1.html", "Comunicaciones I"],
          ["es-hardware-comunicaciones-2.html", "Comunicaciones II"],
          ["es-hardware-comunicaciones-3.html", "Comunicaciones III"],
          ["es-hardware-comunicaciones-4.html", "Comunicaciones IV"],

          ["es-hardware-auxiliares-1.html", "Elementos auxiliares I"],
          ["es-hardware-auxiliares-2.html", "Elementos auxiliares II"],

          ["es-hardware.html", "Test global de Hardware"],
       ]
   },
   {
      "header" : ["software", "Software"],
      "links": [
          ["es-software-intro-1.html", "Introducción al software I"],
          ["es-software-intro-2.html", "Introducción al software II"],
          ["es-software-licencias-1.html", "Licencias de software I"],
          ["es-software-licencias-2.html", "Licencias de software II"],
          ["es-software-sistema-operativo-1.html", "Sistema Operativo I"],
          ["es-software-sistema-operativo-2.html", "Sistema Operativo II"],
          ["es-software-sistema-operativo-3.html", "Sistema Operativo III"],
          ["es-software-sistema-operativo-4.html", "Sistema Operativo IV"],
          ["es-software-sistema-operativo-5.html", "Sistema Operativo V"],
          ["es-software-sistema-operativo-6.html", "Sistema Operativo VI"],
          ["es-software-formatos-imagen-1.html", "Formatos de imagen I"],
          ["es-software-formatos-imagen-2.html", "Formatos de imagen II"],
          ["es-software-formatos-imagen-3.html", "Formatos de imagen III"],
          ["es-software-formatos-imagen-4.html", "Formatos de imagen IV"],
          ["es-software-formatos-imagen-5.html", "Formatos de imagen V"],
          ["es-software-formatos-imagen-6.html", "Formatos de imagen VI"],
          ["es-software.html", "Test global de Software"],
       ]
   },
   {
      "header" : ["ciberseguridad", "Ciberseguridad"],
      "links": [
          ["es-ciberseguridad-amenazas-1.html", "Amenazas de seguridad 1"],
          ["es-ciberseguridad-amenazas-2.html", "Amenazas de seguridad 2"],
          ["es-ciberseguridad-amenazas-3.html", "Amenazas de seguridad 3"],
          ["es-ciberseguridad-amenazas-4.html", "Amenazas de seguridad 4"],
       ]
   },
   {
      "header" : ["tecnologia", "Tecnología y Sociedad"],
      "links": [
          ["es-historia-tecnologia-prehistoria.html", "Historia de la Tecnología. Prehistoria"],
          ["es-historia-tecnologia-antigua.html", "Historia de la Tecnología. Edad Antigua"],
          ["es-historia-tecnologia-moderna.html", "Historia de la Tecnología. Edad Moderna"],
          ["es-historia-tecnologia-revolucion-industrial.html", "Historia de la Tecnología. Revolución Industrial"],
          ["es-historia-tecnologia-siglos-xx-xxi.html", "Historia de la Tecnología. Siglos XX y XXI"],

          ["es-technology-objects-1.html", "Los objetos técnicos y la sociedad I"],
          ["es-technology-objects-2.html", "Los objetos técnicos y la sociedad II"],
          ["es-technology-objects-3.html", "La Normalización I"],
          ["es-technology-objects-4.html", "La Normalización II"],

          ["es-historia-tecnologia.html", "Historia de la Tecnología. Test global"],
          ["es-technology-objects.html", "Los objetos técnicos. Test global"],
       ]
   },
]


index_template = """<!DOCTYPE html>
<html lang="es-es">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

   <!--
   Copyright (c) 2021 Carlos Félix Pardo Martín

   Copyright (c) 2021 James Q Quick
   https://github.com/jamesqquick/Build-A-Quiz-App-With-HTML-CSS-and-JavaScript

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.
   -->

   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta http-equiv="X-UA-Compatible" content="ie=edge">
   <meta name="description" content="Test de Tecnología. Materiales, Mecánica, Electricidad.">
   <title>Test de Tecnología - Picuino</title>
   <link rel="stylesheet" href="app.css">
   
   <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
   <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
   <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">

   <link rel="canonical" href="https://www.picuino.com/test/index.html">

</head>

<body>
   <div class="container">
      <div id="home" class="flex-center flex-column">

        <h1 id="index">TEST DE TECNOLOGÍA</h1>
        {% set sp = namespace(section = 1) %}
        {% for section in data %}
        <a class="btn2" href="#{{section.header[0]}}">{{ sp.section }}. {{ section.header[1] }}</a>
        {%- set sp.section = sp.section + 1 %}
        {%- endfor %}
      
	<hr style="margin:20px 0 20px 0">

	<a class="btn2" href="index-en.html" target="_blank">Test in English</a>
	<a class="btn2" href="https://www.picuino.com/es/" target="_blank">Picuino</a>

	<hr style="margin:20px 0 80px 0">

        {% set sp = namespace(section=1, numtest=1, sumtest=0) %}
        {%- for section in data %}

        <h1 id="{{ section.header[0] }}">{{ section.header[1] }}</h1>
        {%- for link in section.links %}
        <a class="btn" href="{{ link[0] }}">{{ sp.section }}.{{ sp.numtest }} {{ link[1] }}</a>
        {%- set sp.numtest = sp.numtest + 1 %}
        {%- set sp.sumtest = sp.sumtest + 1 %}
        {%- endfor %}
        <a class="btn2" href="#index">Volver al índice</a>
        {%- set sp.section = sp.section + 1 %}
        {%- set sp.numtest = 1 %}
        {%- endfor %}

      </div>
   </div>

   <div class="container">
   
   <!-- FOOTER -->
   <div class="footer">
   <a href="https://www.picuino.com/es/contacto.html" target="_blank">Contacto</a>
   <a href="https://www.picuino.com/es/legal-aviso.html" target="_blank">Aviso legal</a>
   <a href="https://www.picuino.com/es/legal-cookies.html" target="_blank">Política de Cookies</a>
   <a href="https://github.com/picuino/questionary/blob/master/Licenses.md" target="_blank">Créditos</a>
   <a href="https://github.com/picuino/questionary/" target="_blank">GitHub</a>
   <a href="https://www.picuino.com/test/index.html" target="_blank">Índice</a>
   <p>Copyright © 2021 por Carlos Félix Pardo Martín.</p>
   <p>Licencia: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">Creative Commons Attribution-ShareAlike 4.0</a></p>
   <p>{{ sp.sumtest }} Test de Tecnología</p>
   </div>

   </div>
</body>
</html>
"""


def main():
   template = Template(index_template)
   data = template.render(data = index_data)
   with codecs.open("index.html", 'w', encoding="utf-8") as fo:
       fo.write(data)


if __name__ == "__main__":
   main()
