# Exercício 38 – Comparando números

"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma
mensagem: 'O primeiro valor é maior', 'O segundo valor é maior' e 'Não existe valor maior, os dois são iguais'
"""

# Declarando as variáveis
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

# Criando as condições e imprimindo na tela
if num1 > num2:
    print("O primeiro valor é maior.")
elif num1 < num2:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
