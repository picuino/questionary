import codecs
import re

header = """
Category: Mecánica
Title: Medidas con calibre
Copyright: 2022 por Carlos Pardo Martín
License: Creative Commons Attribution-ShareAlike 4.0
License_link: https://creativecommons.org/licenses/by-sa/4.0/
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
    Medida = {%s} mm
"""

data = [header]
for i in range(301):
    medida = '%0.1f' % (i/10.0)
    medida = re.sub('\.', ',', medida)
    question = question_template % (medida, i, medida)
    data.append(question)
with codecs.open('es-mecan-calibre-medidas.yaml', 'w', encoding='utf-8-sig') as fo:
    fo.write(''.join(data))
