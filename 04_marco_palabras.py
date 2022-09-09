# Marco de palabras

"""
* Crea una función que reciba un texto y muestre cada palabra en una línea,
formando un marco rectangular de asteriscos.
¿Qué te parece el reto? Se vería así:

**********
* ¿Qué   *
* te     *
* parece *
* el     *
* reto?  *
**********

"""

print("\n***** Reto 3 *****")
def box(texto):
  lista_texto = texto.split(" ")
  print("Texto: "+ texto)
  list_count_word = [len(word) for word in lista_texto]
  max_word = max(list_count_word)
  print(max_word*"*"+"****")
  for word in lista_texto:
    print("* " + word + (max_word-len(word))*" "+" *")
  print(max(list_count_word)*"*"+"****\n")
frase = "Me gusta el reto"
box(frase)