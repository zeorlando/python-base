#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__='0.1.2'

turmas = {
   'sala1' : ['Pedro', 'Maria', 'Miguel', 'Luana', 'Laura'],
   'sala2' : ['Lucas', 'Mileny', 'José', 'Milton', 'Valentim', 'Alberto']    }


atividade = {
    'Inglês' : ['Pedro', 'José', 'Laura', 'Lucas'],
    'Música' : ['Maria', 'Luana', 'Milton', 'Lucas', 'Mileny'],
    'Dança' : ['Alberto', 'José', 'Mileny', 'Luana', 'Laura'],
}

for nome_atividade, nome_aluno in atividade.items():
   sala1_atividade = set(turmas['sala1']) & set(nome_aluno)
   sala2_atividade = set(turmas['sala2']) & set(nome_aluno)
   
   print('*' * 40)
   print(nome_atividade)
   print('SALA 1',sala1_atividade)
   print('SALA 2',sala2_atividade)

   
