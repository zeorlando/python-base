#/usr/bin/env python3

"""Lista de e-mail"""
__version__ = '0.1.0'
__author__ = 'José Orlando'


email_template = """
Olá, %(nome)s! Tudo bem?

Temos um curso a sua disposição. É o curso de %(curso)s.
Temos ainda %(vaga)d vagas.

Está saindo por apenas %(valor).2f. Garanta já a sua vaga!

CodeForAll por uma sociedade mais igualitária.

Vamos juntos : )
"""

clientes = ['Antonio', 'Altamira', 'Tainá']

for cliente in clientes:
    print(
       email_template
       %{
        'nome': cliente,
        'curso': 'Python',
        'vaga': 3,
        'valor': 200.50,
       }
    )




