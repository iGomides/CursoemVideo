# Exercício 41 – Classificando Atletas

"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade: até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JÚNIOR.
Até 25 anos: SÊNIOR, Acima de 25 anos: MASTER
"""

# Importando bibliotecas
from datetime import date # Módulo que captura ano atual

# Declarando as variáveis
ano = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = ano - nasc

# Definindo e imprimindo o valor da categoria
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")
