import codecs
import re

header = """
Category: Mecánica
Title: Medidas con calibre
Copyright: 2022 Carlos Félix Pardo Martín
License: Creative Commons Attribution-ShareAlike 4.0
License_link: https://creativecommons.org/licenses/by-sa/4.0/
Source_link: https://www.picuino.com/es/mecan-calibre.html
Show_max: 30
Num_tries: 1

---

"""

question_template = """
- Title: Calibre midiendo %s milímetros
  Image: ../images/mecan-calibre-%04dn.png
  Image_width: 800
  Cloze:
    ¿Qué medida está realizando este calibre?
    <br><br>
    Medida = {%s|%s} mm
"""

data = [header]
for i in range(301):
    medida_punto = '%0.1f' % (i/10.0)
    medida_coma = re.sub('\.', ',', medida_punto)
    question = question_template % (medida_coma, i, medida_coma, medida_punto)
    data.append(question)
with codecs.open('es-mecan-calibre-medidas.yaml', 'w', encoding='utf-8-sig') as fo:
    fo.write(''.join(data))
