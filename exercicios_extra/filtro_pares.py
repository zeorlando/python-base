"""
A partir da lista numeros = list(range(1, 21)), 
crie uma nova lista contendo apenas os números pares, usando list comprehension.
"""

lista_numeros = list(range(1, 21))

lista_com_pares = [par for par in lista_numeros if par % 2 == 0]

print(lista_com_pares)