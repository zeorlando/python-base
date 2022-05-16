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
__version__ = '0.0.1'
__author__ = 'José Orlando'
__license__ = 'Unlicense'


import os

current_language = os.getenv('LANG')[:5]

msg = 'Hello, World!'

if current_language == 'pt_BR':
    msg = 'Olá, mundo!'
elif current_language == 'it_IT': 
    msg = 'Ciao, mondo!'
print(msg)
