contador = 0

def incrementa_contador():
    #... começa escopo local
    # assignment '=' '+=' '-='
    global contador
    contador += 1

incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()

print(contador)
