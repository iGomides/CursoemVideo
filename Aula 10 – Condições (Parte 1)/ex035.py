# Exercício 35 – Analisando Triângulo v1.0
# Crie um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo.

lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Pode formar um triângulo!")
else:
    print("Não pode formar um triângulo!")
