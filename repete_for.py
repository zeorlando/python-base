#!/usr/bin/env python3


# For loops / laço for
original = [1, 2, 3]
lista_dobrada = []
for item in original:
    lista_dobrada.append(item * 2)

print(lista_dobrada)

# Funcional

triplicada = [n * 3 for n in original]
print(triplicada)
