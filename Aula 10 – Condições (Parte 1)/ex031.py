# Exercício 31 – Custo da Viagem

"""
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

dist = float(input("Quantos qulômetros? "))
precokm = 0.50

if dist > 200:
    precokm = 0.45

print("O valor da sua viagem ficou em R${:.2f}.".format(dist * precokm))
