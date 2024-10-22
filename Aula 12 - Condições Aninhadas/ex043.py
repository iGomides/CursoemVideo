# Exercício 43 – Índice de Massa Corporal

"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

    • Abaixo de 18,5: Abaixo do Peso
    • Entre 18,5 e 25: Peso Ideal
    • De 25 até 30: Sobrepeso
    • De 30 até 40: Obesidade
    • Acima de 40: Obesidade Mórbida
"""

# Declarando variáveis e recebendo a entrada dos dados
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = peso / (altura ** 2) # Calculando o IMC

#  Imprimindo o resultado
print(f"Seu IMC é: {imc:.2f}")
if imc <= 18.5:
    print("Está ABAIXO DO PESO.")
elif imc <= 25:
    print("Está no PESO IDEAL.")
elif imc <= 30:
    print("Está com SOBREPESO.")
elif imc <= 40:
    print("Está com OBESIDADE.")
else:
    print("Cê vai morrer!")
