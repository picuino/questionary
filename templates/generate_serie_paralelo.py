text = """
- Title: Serie, Paralelo o Cortocircuito %02d
  Question: ¿Cómo está conectado el siguiente circuito?
  Image: images/electric-serie-paralelo-c%02d.png
  Image_width: 320
  Choices:
    - En paralelo
    - En serie
    - Tiene un cortocircuito en la pila
    - Tiene un cortocircuito en una bombilla"""

for i in range(1, 41):
    print(text % (i, i))
print()
