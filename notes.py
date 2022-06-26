#!/usr/bin/env python3

"""Bloco de notas

$ notes.py new 'Minha nota'
tag: tech
text: 
Anotação geral

$ notes.py read tag=tech
...
...

"""
__version__ = '0.1.0'

import os
import sys

path = os.curdir
filepath = os.path.join(path, 'notes.txt')

arguments = sys.argv[1:]

if not arguments: 
    print('Para uma nova nota escolha: new Título da nota')
    print('Para ler uma nota existente: read título da tag')
    sys.exit(1)

if arguments[0] == 'new':
    title = arguments[1]
    text = [
        f'{title}',
        input('tag: ').strip(),
        input('text: \n').strip(),
    ]
    with open(filepath, 'a') as file_:
        file_.write('\t'.join(text) + '\n')

if arguments[0] == 'read':
    for line in open(filepath):
        title, tag, text = line.split('\t')
        if tag.lower() == arguments[1].lower():
            print(f'{title}')
            print(f'{text}')
            print('-' * 30)
            print()

        

