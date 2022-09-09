# Numeros perdidos

"""
Enunciado: Dado un array de enteros ordenado y sin repetidos, 
crea una función que calcule y retorne todos los que faltan entre
el mayor y el menor.
- Lanza un error si el array de entrada no es correcto.
"""

print("\n***** Reto 1 *****")
list_1 = [3,7,8,12,14]
new_list = []
iterate = min(list_1) + 1
while iterate != max(list_1):
  check_list = [iterate == i for i in list_1]
  if sum(check_list) == 0:
    new_list.append(iterate)
  iterate += 1
print(f"List introduced: {list_1}")
print(f"The missing numbers are: {new_list}\n")