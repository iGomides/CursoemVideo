# Exercício 34 – Aumentos múltiplos

"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input("Qual o sálário do funcionário? R$"))
novosalario = 0

if salario <= 1250:
    novosalario = salario * 1.15
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novosalario:.2f}.")
else:
    novosalario = salario * 1.10
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novosalario:.2f}.")
