nome = 'global'

def escopo():
    nome = 'local'
    print(nome)
    return nome

print(nome)
escopo()
