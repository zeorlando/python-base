#!/usr/bin/env python3

'''
Exemplos de funções
'''

'''
f(x) = 5 * (x/2)
'''

def funcao_propria(x):
    return 5 * (x/2)

def double(x):
    return x * 2

print(funcao_propria(10))
print(double(funcao_propria(10)))

###

def print_in_upper(text):
    print(text.upper())

print_in_upper('lucas')

###

def heron(a, b, c):
    '''Calcula a área de um triângulo'''
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s-a) * (s-b) * (s-c)
    return area ** 0.5 # math.sqrt(area)

def heron2(params):
    return heron(*params)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (12, 35, 37)
]

#print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron2(t)
    print(f'A área do triangulo é: {area}')
