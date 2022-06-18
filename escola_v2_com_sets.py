#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__='0.1.1'

sala1 = ['Pedro', 'Maria', 'Miguel', 'Luana', 'Laura']
sala2 = ['Lucas', 'Mileny', 'José', 'Milton', 'Valentim', 'Alberto']


aula_ingles = ['Pedro', 'José', 'Laura', 'Lucas']
aula_musica = ['Maria', 'Luana', 'Milton', 'Lucas', 'Mileny']
aula_danca = ['Alberto', 'José', 'Mileny', 'Luana']

atividades =  [
    ('Inglês', aula_ingles), 
    ('Música',aula_musica), 
    ('Dança', aula_danca),
]

for nome_atividade, atividade in atividades:

    atividade_sala1 = set(sala1) & set(atividade) 
    atividade_sala2 = set(sala2) & set(atividade)

    print(f'{nome_atividade} sala 1 - ', atividade_sala1)
    print(f'{nome_atividade} sala 2 - ', atividade_sala2)
    print('*' * 46)


