#
#  Program to convert cloze test from YAML format to html format and
#  Moodle XML format.
#
#  Index maker (c) 2022 Carlos Pardo
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
         ["es-material-properties.html", "Propiedades de los materiales"],
         ["es-material-wood.html", "La madera"],
         ["es-material-metals.html", "Los metales"],
         ["es-material-plastics.html", "Los plásticos"],
         ["es-material-stone.html", "Los materiales pétreos"],
         ["es-material.html", "Test global de materiales"],
      ]
   },
   {
      "header" : ["electricidad", "Electricidad"],
      "links": [
         ["es-electric-introduction.html", "Fundamentos"],
         ["es-electric-components-type.html", "Tipos de componentes"],
         ["es-electric-components-name.html", "Nombre de componentes (test)"],
         ["es-electric-components-name-cloze.html", "Nombre de componentes (cloze)"],

         ["es-electric-color-code-1.html", "Código de colores 1"],
         ["es-electric-color-code-2.html", "Código de colores 2"],

         ["es-electric-units-change.html", "Cambio de unidades"],
         ["es-electric-units-magnitudes.html", "Unidades y Magnitudes"],
         ["es-electric-circuits.html", "Circuitos eléctricos"],

         ["es-electric-ohms-law.html", "Ley de Ohm. Fundamentos"],
         ["es-electric-ohms-law-2.html", "Ley de Ohm. Cálculos"],

         ["es-electric-series-parallel-identify.html", "Identificar serie y paralelo"],
         ["es-electric-series-parallel-calc.html", "Calcular serie y paralelo"],
         ["es-electric-series-parallel-calc-2.html", "Calcular resistencia equivalente"],

         ["es-electric-power.html", "Potencia"],
         ["es-electric-energy.html", "Energía"],
         ["es-electric-breadboard.html", "Breadboard"],
         ["es-electric-digital.html", "Electrónica digital"],
       ]
   },
   {
      "header" : ["hardware", "Hardware y Software"],
      "links": [
           ["es-hardware-intro.html", "Introducción al hardware"],
           ["es-hardware-unidades.html", "Unidades de medida"],
           ["es-hardware-ley-moore.html", "Ley de Moore"],
           ["es-hardware-pc.html", "Hardware del ordenador personal"],
           ["es-hardware-placa-base.html", "Placa base"],
       ]
   },
   {
      "header" : ["controladores", "Control Automático"],
      "links": [
           ["es-control-introduction.html", "Introducción al control automático"],
       ]
   },
   {
      "header" : ["maquinas", "Máquinas y Mecanismos"],
      "links": [
           ["es-machines-simple.html", "Máquinas simples"],
           ["es-machines-transmission1.html", "Mecanismos de<br>transmisión I"],
           ["es-machines-transmission2.html", "Mecanismos de<br>transmisión II"],
           ["es-machines-transmission3.html", "Mecanismos de<br>transmisión III"],
           ["es-machines-transformation1.html", "Mecanismos de<br>transformación I"],
           ["es-machines-transformation2.html", "Mecanismos de<br>transformación II"],
           ["es-machines.html", "Test global de Máquinas y Mecanismos"],
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
      "header" : ["tecnologia", "Tecnología y Sociedad"],
      "links": [
           ["es-technology-society-history.html", "Historia de la tecnología"],
           ["es-technology-society-objects.html", "Los objetos técnicos y la sociedad"],
       ]
   },
]


index_template = """<!DOCTYPE html>
<html lang="es-es">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

   <!--
   Copyright (c) 2021 Carlos Pardo

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
   
   <link rel="icon" type="image/png" href="favicon-16.png" sizes="16x16">
   <link rel="icon" type="image/png" href="favicon-48.png" sizes="48x48">
   <link rel="icon" type="image/png" href="favicon-96.png" sizes="96x96">
   
</head>

<body>
   <div class="container">
      <div id="home" class="flex-center flex-column">

        <h1>TEST DE TECNOLOGÍA</h1>
        {% for section in data %}
        <a class="btn" href="#{{section.header[0]}}">{{ section.header[1] }}</a>
        {%- endfor %}
      
		  <hr style="margin:20px 0 20px 0">
        <a class="btn" href="end.html">Última puntuación</a>
	     <a class="btn" href="index_en.html">Test in English</a>
	     <a class="btn" href="https://www.picuino.com/">Picuino</a>
		  <hr style="margin:20px 0 80px 0">

        {% set sp = namespace(counter = 1) %}
        {%- for section in data %}

        <h1 id="{{ section.header[0] }}">{{ section.header[1] }}</h1>
        {%- for link in section.links %}
        <a class="btn" href="{{ link[0] }}">{{ sp.counter }}. {{ link[1] }}</a>
        {%- set sp.counter = sp.counter + 1 %}
        {%- endfor %}
        {%- endfor %}

        <p style="margin-top:80px"></p>

      </div>
   </div>


   <div class="container">
   
   <!-- FOOTER -->
   <div class="footer">
   <a href="https://www.picuino.com/es/contacto.html">Contacto</a>
   <a href="https://www.picuino.com/es/legal-aviso.html">Aviso legal</a>
   <a href="https://www.picuino.com/es/legal-cookies.html">Política de Cookies</a>
   <a href="https://github.com/picuino/questionary/blob/master/Licenses.md">Créditos</a>
   <a href="https://github.com/picuino/questionary/">GitHub</a>
   <a href="https://www.picuino.com/test/index.html">Índice</a>
   </div>

   <!-- Cookies Advise -->
   <div id="cookiesbar" style="display: none">
   Esta página web utiliza cookies propias y de terceros 
   para propósitos funcionales y de análisis de navegación.
   Puedes obtener más información en nuestra 
   <a href="https://www.picuino.com/es/legal-cookies.html" 
   target="_blank">política de Cookies.</a><br>
   Si continúas navegando, aceptas su uso.
   <br>
   <a href="javascript:void(0);" onclick="cookieBarAcceptRequired();">Aceptar Necesarias</a> |
   <a href="javascript:void(0);" onclick="cookieBarAcceptAll();"><b>ACEPTAR TODAS</b></a>
   </div>
   <script>
   if (document.cookie.indexOf("cookiesBar")<0) {cookieBarDisplay("block");}
   function cookieBarAcceptAll(){setCookie("cookiesBar","1",60); cookieBarDisplay("none");}
   function cookieBarAcceptRequired(){setCookie("cookiesBar","1",60); cookieBarDisplay("none"); setCookie("noAnalyticalCookies","1",60); }
   function cookieBarDisplay(dsp){document.getElementById("cookiesbar").style.display=dsp;}
   function setCookie(cname, cvalue, exdays){var d=new Date();d.setTime(d.getTime()+(exdays*24*3600000));document.cookie=cname+"="+cvalue+"; "+"expires="+d.toUTCString()+"; path=/;";}
   </script>

   <!-- Matomo -->
   <script>
   if (document.cookie.indexOf("noAnalyticalCookies")<0) {
     var _paq = window._paq = window._paq || [];
     _paq.push(['trackPageView']);
     _paq.push(['enableLinkTracking']);
     (function() {
       var u="//www.picuino.com/matomo/";
       _paq.push(['setTrackerUrl', u+'matomo.php']);
       _paq.push(['setSiteId', '1']);
       var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
       g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
     })();
   }
   </script>
   <!-- End Matomo Code -->

   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=UA-59765999-1"></script>
   <script>
   if (document.cookie.indexOf("noAnalyticalCookies")<0) {
     window.dataLayer=window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);} 
     gtag('js', new Date()); gtag('config', 'UA-59765999-1');
   }
   </script>

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
