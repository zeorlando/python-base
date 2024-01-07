#!/usr/bin/env python3

'''
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

temp maior que 30 e temp vezes 3 for maior ou igual a umidade:

"ALERTA!!! 🥵♒ Perigo de calor úmido"

temp entre 10 e 30: "😀 Normal"

temp entre 0 e 10: "🥶 Frio"

temp <0: "ALERTA!!! ⛄ Frio Extremo."
'''
import sys
import logging 
log = logging.Logger('Alerta')

info = {
    'temperatura':None,
    'umidade':None,
}

while True:
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break

    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key] = float(input(f'{key}: ').strip())
        except ValueError:
            log.error(f'{key.capitalize()} invalida')  
            sys.exit(1)

temperatura, umidade = info.values()

if temperatura > 50:
    print('ALERTA!!! 🥵 Perigo calor extremo')
elif temperatura >= 10 and temperatura <= 30:
    print('😀 Normal')
elif temperatura >= 0 and temperatura <= 10:
    print('🥶 Frio')
elif temperatura < 0:
    print('ALERTA!!! ⛄ Frio Extremo.')
elif temperatura * 3 >= umidade: 
    print('ALERTA!!! 🥵♒ Perigo de calor úmido')

