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
import logging
from logging import handlers 

log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()
log = logging.Logger('ze', log_level)
#ch = logging.StreamHandler()
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    'meulog.log',
    maxBytes=300, 
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh)

arguments = {
    'lang':None,
    'count':1,
}
for arg in sys.argv[1:]:
    try:
        key, value = arg.split('=')
    except ValueError as e:
        log.error(
            'You need to use "=", you passed %s, try --key=value: %s',
            arg,
            str(e)
        )
        sys.exit(1)
        
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

try: 
    message = msg[current_language]
except KeyError as e:
    print(f'[ERROR] {str(e)}')
    print(f'Language is invalid, choose from: {list(msg.keys())}')
    sys.exit(1)

print(message * int(arguments['count']))
