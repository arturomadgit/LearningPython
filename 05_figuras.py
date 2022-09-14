"""
Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
"""

print("\n***** Reto 4 *****")
lado = 5
figura = "Triangulo"
print(f"{figura} de lado {lado}")
lineas = 1
while lineas<=lado:
  if figura == "Cuadrado":
    print(lado * "*")
  elif figura == "Triangulo":
    print((lado - lineas)* " " + ((lineas*2)-1)*"*" + (lado - lineas)* " ")
  lineas += 1