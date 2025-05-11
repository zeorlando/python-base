"""
Crie uma lista de tuplas (x, x**2) para os números de 1 a 15, 
somente se o quadrado for múltiplo de 3
"""

numeros = range(1,16)

lista_tupla = [(numero, numero**2) for numero in numeros if numero % 3 == 0]

print(lista_tupla)