# Exercício 22 – Analisador de Textos

"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

name = str(input("Informe seu nome: ")).strip()

print(name.upper())
print(name.lower())

nospace = name.split()
nospace = ''.join(nospace)
print(nospace.__len__())

print(name.find(' '))
