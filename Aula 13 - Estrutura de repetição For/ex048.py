# Exercício 48 – Soma ímpares múltiplos de três

"""
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
"""

inicio = 3
fim = 500
soma = 0

for contagem in range(inicio, fim + 1, 3):
    if contagem % 2 == 1:
        soma += contagem
    print(contagem, end=' ')
print('Acabou')
print(f'A soma de todos este números é {soma}')
