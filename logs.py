#!/usr/bin/env python3

import os 
import logging
from logging import handlers 

log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()

#TODO transformar em função
#TODO usar lib (loguru)
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

'''
log.debug('Mensagem para o dev, qe, sysadmin')
log.info('Mensagem geral para usuários')
log.warning('Aviso que não causa erro')
log.error('Erro que afeta uma única execução')
log.critical('Erro geral. O banco de dados sumiu.')
'''

print('---')

try:
    1/0
except ZeroDivisionError as e:
    log.error('Deu erro %s', str(e))
