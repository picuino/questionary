"""Imprime una lista de las nuevas imágenes que no aparecen en
el fichero Licenses.md, para poder añadirlas."""

import os
import codecs
import re

licenses = codecs.open('../Licenses.md', 'r', encoding='utf-8').read()

images = [f for f in os.listdir('.') if f[-4:].lower() in ['.png', '.gif', '.jpg']]

for image in images:
    if not re.search('images/thumbs/' + image, licenses):
        print('![](images/thumbs/%s)' % image)

input()
