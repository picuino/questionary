import codecs

header = """
Category: Mecánica
Title: Medidas con calibre
Copyright: 2022 por Carlos Pardo Martín
License: Creative Commons Attribution-ShareAlike 4.0
License_link: https://creativecommons.org/licenses/by-sa/4.0/
Show_max: 30

---

"""

question = """
- Title:
  Image: ../images/mecan-calibre-%04dn.png
  Image_width: 800
  Cloze:
    ¿Qué medida está tomando este calibre?
    <br><br>
    Medida = {%0.1f} mm
"""

data = [header] + [question % (i, i/10.0) for i in range(301)]
with codecs.open('es-mecan-calibre-medidas.yaml', 'w', encoding='utf-8-sig') as fo:
    fo.write(''.join(data))
