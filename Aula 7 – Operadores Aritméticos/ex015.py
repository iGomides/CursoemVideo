# Exercício 15 – Aluguel de Carros

"""
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.
"""

dia = float(input("Diárias utilizadas: "))
km = float(input("Quilometragem rodada: "))

vdia = (dia * 60)
vkm = (km * 0.15)
vtotal = (vdia + vkm)

print("O valor total a pagar é de R${:.2f}. Sendo R${:.2f} de diarias e {:.2f} de quilometragem.".format(vtotal, vdia, vkm))
