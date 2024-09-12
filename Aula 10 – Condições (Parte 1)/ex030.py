# Exercício 30 – Par ou Ímpar?

"""
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.
"""

numero = int(input("Digite um número: "))

divisor = 2
resto = numero % divisor

if resto == 0:
    print("O número em questão é par.")
else:
    print("O número em questão é ímpar.")
