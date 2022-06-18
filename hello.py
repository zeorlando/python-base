#!/usr/bin/env python3

"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe
a correspondete.

Como usar:

Tenha a varíavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = '0.1.3 '
__author__ = 'José Orlando'
__license__ = 'Unlicense'


import os
import sys

arguments = {
    'lang':None,
    'count':1,
}
for arg in sys.argv[1:]:
    #TODO Tratar value error
    key, value = arg.split('=')
    key = key.lstrip('-').strip()
    value = value.strip()
    if  key not in arguments:
        print(f'Invalid option {key}')
        sys.exit()
    arguments[key] = value

            
current_language = arguments['lang']
if current_language is None:
   current_language = os.getenv('LANG', 'en_US')[:5]

msg = {
    'pt_BR' : 'Olá, Mundo!',
    'en_US' : 'Hello world!',
    'it_IT' : 'Ciao, mondo!',
    'es_ES' : 'Hola, mundo!',
    'fr_FR' : 'Bonjour, Monde!',
}

print(msg[current_language] * int(arguments['count']))
