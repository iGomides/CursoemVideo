# Exercício 12 – Calculando Descontos

"""
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""
from time import perf_counter

preco = float(input("Valor do produto: "))
desconto = (preco * 0.05)
v_final = (preco - desconto)

print("O desconto é de R${} e o valor final é de R${:.2f}.".format(desconto, v_final))