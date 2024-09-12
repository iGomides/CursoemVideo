# Exercício 23 – Separando dígitos de um número

"""
Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados.
"""

num = str(input("Digite um número entre 0 e 9999: "))

uni = (num[3])
dez = (num[2])
cem = (num[1])
mil = (num[0])

print("Unidade:{}".format(uni))
print("Dezena:{}".format(dez))
print("Centena:{}".format(cem))
print("Milhar:{}".format(mil))
