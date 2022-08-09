#!/usr/bin/env python3

import os
import sys
import logging

from logging import handlers
from datetime import datetime

log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()
log = logging.Logger('ze', log_level)
fh = handlers.RotatingFileHandler(
    'log_infixcalc.log',
    maxBytes=300,
    backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

arguments = sys.argv[1:]

if not arguments:
    operation = input('operação: ')
    n1 = input('n1: ')
    n2 = input('n2: ')
    arguments = [operation, n1, n2]    
elif len(arguments) != 3:
    print('Número de argumentos inválido')
    print('ex: [operacao] [n1] [n2]')
    sys.exit(1)

operation, *nums = arguments

valid_operations = ('sum', 'sub', 'mul', 'div')
if operation not in valid_operations:
    print('Operação invalida')
    print('use sum, sub, mul ou div')
    sys.exit(1)

valid_nums = []
for num in nums:
    if not num.replace('.', '').isdigit():
        print('Número invalido')
        sys.exit(1)
    if '.' in num:
        num = float(num)
    else:
        num = int(num)
    valid_nums.append(num)

n1, n2 = valid_nums

if operation == 'sum':
    result = n1 + n2;
elif operation == 'sub':
    result = n1 - n2
elif operation == 'mul':
    result = n1 * n2
elif (operation == 'div'):
    if n2 == 0:
        print('Não é possível dividir por 0')
        sys.exit(1)
    else:
        result = n1 / n2

path = os.curdir
filepath = os.path.join(path, 'infixcalc.log')
timestamp = datetime.now().isoformat()

with open(filepath, 'a') as file_:
    file_.write(f'{timestamp} | {operation}, {n1}, {n2} = {result}\n')


if result != None:
    print(f'O resultado é {result}')

    

#print(arguments)
#print(valid_nums)
