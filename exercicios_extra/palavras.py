""" 
Dada a lista palavras = ["casa", "elefante", "sol", "paralelepípedo", "rio", "montanha"], 
use list comprehension para gerar uma nova lista com apenas as palavras que têm mais de 5 letras.
"""

palavras = ["casa", "elefante", "sol", "paralelepípedo", "rio", "montanha"]

palavras_mais_cinco_letras = [cinco_letras for cinco_letras in palavras if len(cinco_letras) > 5]

print(palavras_mais_cinco_letras)