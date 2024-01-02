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
      "header" : ["electricity", "Electricity"],
      "links": [
          ["en-electric-components-name.html", "Name of components (test)"],

          ["en-electric-color-code-1.html", "Color code 1"],
          ["en-electric-color-code-1.html", "Color code 2"],

          ["en-electric-series-parallel-identify.html", "Series and parallel identification"],

          ["en-electric-energy-calc.html", "Electrical energy calculations"],
      ]
   },
]


index_template = """<!DOCTYPE html>
<html lang="en">
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

</head>

<body>
   <div class="container">
      <div id="home" class="flex-center flex-column">

        <h1 id="index">TECHNOLOGY TEST</h1>
        {% set sp = namespace(section = 1) %}
        {% for section in data %}
        <a class="btn2" href="#{{section.header[0]}}">{{ sp.section }}. {{ section.header[1] }}</a>
        {%- set sp.section = sp.section + 1 %}
        {%- endfor %}
      
	<hr style="margin:20px 0 20px 0">
	<a class="btn2" href="index.html" target="_blank">Test en Español</a>
	<a class="btn2" href="https://www.picuino.com/en/" target="_blank">Picuino</a>
	<hr style="margin:20px 0 80px 0">

        {% set sp = namespace(section=1, numtest=1, sumtest=0) %}
        {%- for section in data %}

        <h1 id="{{ section.header[0] }}">{{ section.header[1] }}</h1>
        {%- for link in section.links %}
        <a class="btn" href="{{ link[0] }}">{{ sp.section }}.{{ sp.numtest }} {{ link[1] }}</a>
        {%- set sp.numtest = sp.numtest + 1 %}
        {%- set sp.sumtest = sp.sumtest + 1 %}
        {%- endfor %}
        <a class="btn2" href="#index">Back to index</a>
        {%- set sp.section = sp.section + 1 %}
        {%- set sp.numtest = 1 %}
        {%- endfor %}

        <p style="margin-top:80px"></p>

      </div>
   </div>


   <div class="container">
   
   <!-- FOOTER -->
   <div class="footer">
   <a href="https://www.picuino.com/en/contacto.html" target="_blank">Contact</a>
   <a href="https://www.picuino.com/es/legal-aviso.html" target="_blank">Terms Of Service</a>
   <a href="https://www.picuino.com/en/legal-cookies.html" target="_blank">Cookie policy</a>
   <a href="https://github.com/picuino/questionary/blob/master/Licenses.md" target="_blank">Credits</a>
   <a href="https://github.com/picuino/questionary/" target="_blank">GitHub</a>
   <a href="https://www.picuino.com/test/index.html" target="_blank">Index</a>
   <p>Copyright © 2021 by Carlos Félix Pardo Martín.</p>
   <p>Licencia: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">Creative Commons Attribution-ShareAlike 4.0</a></p>
   <p>{{ sp.sumtest }} Technology test</p>
   </div>

   <!-- Cookies Advise -->
   <div id="cookiesbar" style="display: none">
   This website uses its own and third party cookies for functional and navigation analysis purposes.
   You can get more information on our <a href="https://www.picuino.com/es/legal-cookies.html" target="_blank">Cookie policy.</a> <br> 
   If you continue browsing, you accept its use.
   <br>
   <a href="javascript:void(0);" onclick="cookieBarAcceptRequired();">Only required</a> |
   <a href="javascript:void(0);" onclick="cookieBarAcceptAll();"><b>ACCEPT AND CONTINUE</b></a>
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

   </div>
</body>
</html>
"""


def main():
   template = Template(index_template)
   data = template.render(data = index_data)
   with codecs.open("index-en.html", 'w', encoding="utf-8") as fo:
       fo.write(data)

if __name__ == "__main__":
   main()
