# Exercício 26 – Primeira e última ocorrência de uma string

"""
Faça um programa que leia uma frase pelo teclado e mostre
quantas vezes aparece a letra “A”, em que posição ela aparece
a primeira vez e em que posição ela aparece a última vez.
"""


frase = str(input('Digite uma frase: ')).lower()

print("A frase possui {} letras 'a'.".format(frase.count('a')))
print("A letra 'a' aparece primeiro na posição {}.".format(frase.find('a') + 1))
print("A letra 'a' aparece por ultimo na posição {}.".format(frase.rfind('a') + 1))
