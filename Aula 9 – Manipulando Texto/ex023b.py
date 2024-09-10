# Exercício 23 – Separando dígitos de um número

"""
Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados.
"""

num = str(input("Digite um número entre 0 e 9999: "))

uni = int(num[3])
dez = int(num[2])
cem = int(num[1])
mil = int(num[0])

print("Unidade:{}".format(uni))
print("Dezena:{}".format(dez))
print("Centena:{}".format(cem))
print("Milhar:{}".format(mil))
