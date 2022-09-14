"""
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
"""

print("\n***** Reto 5 *****")
num = 8208
total_num = 0
list_num = [int(x) for x in str(num)]
for i in list_num:
  partial = i ** len(list_num)
  total_num += partial
if num == total_num:
  print(f"El numero {num} es narcisista")
else:
  print(f"El numero {num} no es narcisista")