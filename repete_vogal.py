#!/usr/bin/env python3

lista_palavras = []

while True:
    palavra = input('Digite uma palavra: ').strip()
    if not palavra:
        break
    palavra_final = ''
    
    for letra in palavra:
        #TODO remover acentuacao usando funcao
        '''
        if letra in "AEIOUaeiou":
            palavra_final += letra * 2
        else:
            palavra_final += letra
        '''
        
        palavra_final += letra * 2 if letra in "AEIOUaeiou" else letra 
            
    lista_palavras.append(palavra_final)

print(*lista_palavras, sep='\n')
            
