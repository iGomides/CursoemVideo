# Exercício 29 – Radar eletrônico

"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite.
"""

vel_atual = int(input("Velocidade do veículo: "))
vel_max = 80
valor_multa = (vel_atual - vel_max) * 7

if vel_atual > vel_max:
    print("Você foi multado, aspirante a SpeedRacer!")
    print("O Valor da multa é R${}.".format(valor_multa))
else:
    print("Boa viagem.")
