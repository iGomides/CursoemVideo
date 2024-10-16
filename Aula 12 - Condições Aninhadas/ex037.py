# Exercício 37 – Conversor de Bases Numéricas

"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

# Declarando as variáveis
inteiro = int(input("Informe um número inteiro: "))
escolha = "1"
resultado = 0

# Apresentando as opções de conversão e coletando a escolha
print("Escolha uma das bases para conversão:")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")
escolha = str(input("Sua opção: "))

# Calculando e printando o resultado com base na escolha
if escolha == "1":
    resultado = bin(inteiro)[2:]  # Remove o "0b"
    print(f"{inteiro} convertido para BINÁRIO é igual a {resultado}.")
elif escolha == "2":
    resultado = oct(inteiro)[2:]  # Remove o "0o"
    print(f"{inteiro} convertido para OCTAL é igual a {resultado}.")
elif escolha == "3":
    resultado = hex(inteiro)[2:]  # Remove o "0x"
    print(f"{inteiro} convertido para HEXADECIMAL é igual a {resultado}.")
else:
    print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
