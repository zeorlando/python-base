#/usr/bin/env python3

"""Lista de e-mail"""
__version__ = '0.1.1'
__author__ = 'José Orlando'



import sys
import os

arguments = sys.argv[1:]
if not arguments:
   print('Informe o nome do arquivo de e-mails: ')
   sys.exit(1)
   
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    name, email = line.split(',')
   
   #TODO: Substituir por envio de e-mail 
    print(f'Enviando e-mail para: {email}')
    print()
    print(
       open(templatepath).read()
       %{
        'nome': name,
        'curso': 'Python',
        'vaga': 3,
        'valor': 200.50,
       }
    )
    print('-' * 50)




