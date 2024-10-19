# Exercício 40 – Aquele clássico da Média

"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida: Média abaixo de 5,0: REPROVADO, Média entre 5,0 e 6,9: RECUPERAÇÃO,
Média 7.0 ou superior: APROVADO
"""

# Declarando as variáveis
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2 # Calculando a média

# Imprimindo o resultado
if media >= 7:
    print("Aprovado.")
elif media >= 5 and media <= 6.9:
    print("Recuperação.")
elif media < 5:
    print("Reprovado.")
