# Exercício 13 – Reajuste Salarial

"""
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""

satual = float(input("Salário atual: "))
aumento = (satual * 0.15)
snovo = (satual + aumento)

print("O novo salário será de: R${:.2f}.".format(snovo))
