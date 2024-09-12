# Exercício 22 – Analisador de Textos

"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

name = str(input("Informe seu nome: ")).strip()

print("O nome em maiúsculas fica: {}.".format(name.upper()))
print("O nome em minúsculas fica: {}.".format(name.lower()))

nospace = name.split()
nospace = ''.join(nospace)
print("Ao todo tem {} letras.".format(nospace.__len__()))

print("O primeiro nome tem {} letras.".format(name.find(' ')))
