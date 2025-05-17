'''
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
'''
import sys
import logging

RESERVAS_FILE = 'reservas.txt'
QUARTOS_FILE = 'quartos.txt'

ocupados = {}
try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto,  dias = line.strip().split(',')
        ocupados[int(num_quarto)] = {
            'nome_cliente':nome_cliente,
            'dias': int(dias)
        }
except FileNotFoundError:
    logging.error('Arquivo %s não existe', RESERVAS_FILE)
    sys.exit(1)


# TODO fazer função para ler os arquivos
quartos = {}
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(',')
        quartos[int(num_quarto)] = {
            'nome_quarto':nome_quarto,
            'preco':float(preco), #TODO: decimal
            'disponivel': False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error('Arquivo %s não existe', QUARTOS_FILE)
    sys.exit(1)

print('*' * 52)
print('SISTEMA DE RESERVAS')
print('*' * 52)

if len(ocupados) == len(quartos): 
    print('Hotel lotado')
    sys.exit(0)

nome_cliente = input('Nome do cliente: ').strip()
print()
print('Lista de quartos')
print()
head = ['Número', 'Nome do Quarto', 'Preço', 'Disponível']
print(f'{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<9}')

for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto['nome_quarto']
    preco = dados_quarto['preco']
    disponivel = '⛔' if not dados_quarto['disponivel'] else '👍'
    #TODO: substituir casa decimal por virgula
    print(f'{num_quarto:<6} - {nome_quarto:<14} - R${preco:<9.2f} - {disponivel:<9}')

print('*' * 52)

try:
    num_quarto = int(input('Nº do quarto: ').strip())
    if not quartos[num_quarto]['disponivel']:
        print(f'O quarto {num_quarto} está ocupado.')
        sys.exit(1)
except ValueError:
    logging.error('Número invalido, digite apenas dígitos.')
    sys.exit(1)
except KeyError:
    print(f'Quarto {num_quarto} inesxistente, verifique a lista.')
    sys.exit(1)

try:
    dias = int(input('Quantos dias: ').strip())
except ValueError:
    logging.error('Número invalido, digite apenas dígitos.')
    sys.exit(1)

nome_quarto = quartos[num_quarto]['nome_quarto']
preco_quarto = quartos[num_quarto]['preco']
total = preco_quarto * dias

print(f'{nome_cliente}, você escolheu o {nome_quarto} e vai custar R${total:.2f}')

if input('Confirma? (digite y)').strip().lower() in ('y', 'yes', 'sim', 's'):
    with open(RESERVAS_FILE, 'a') as reserva_file:
        reserva_file .write(f'{nome_cliente},{num_quarto},{dias}\n')



