# Exercício 39 – Alistamento Militar

"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

# Declarando e iniciando as variáveis e constantes
atual = date.today().year

sexo = str(input("Qual o sexo da pessoa? Responda com 'F' para feminino e 'M' para masculino:")).strip().upper()
nascimento = int(input("Ano de nascimento: "))

# Identificando o sexo da pessoa
if sexo == "M" or sexo == "F":
    idade = atual - nascimento
    if sexo == "M":
        if idade == 18:
            print("Deve se alistar nesse ano.")
        elif idade < 18:
            print(f"Menor de 18 anos. Deve se apresentar em {nascimento + 18}.")
        elif idade > 18:
            print(f"Maior de 18 anos, deveria ter se apresentado em {nascimento + 18}.")
    elif sexo == "F":
        print("O alistamento militar não é obrigatório para mulheres, independente da idade.")
else:
    print("Resposta inválida!")
