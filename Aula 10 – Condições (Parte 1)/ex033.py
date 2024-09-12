# Exercício 33 – Maior e menor valores
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Informe o valor I: "))
num2 = int(input("Informe o valor II: "))
num3 = int(input("Informe o valor III: "))

# Inicializando as variáveis maior e menor
maior = num1
menor = num1

# Verificando o maior valor
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Verificando o menor valor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
