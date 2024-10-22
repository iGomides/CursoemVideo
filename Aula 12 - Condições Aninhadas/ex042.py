# Exercício 42 – Analisando Triângulos v2.0

"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado: EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente. ESCALENO: todos os
lados diferentes.
"""

# Declarando as variáveis
lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))

# Calculando a possibilidade de formar triângulo e definindo qual é o modelo.
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Pode formar um triângulo EQUILÁTERO!")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("Pode formar um triângulo ISÓCELES.")
    else:
        print("Pode formar um triângulo ESCALENO.")
else:
    print("Não pode formar um triângulo!")
