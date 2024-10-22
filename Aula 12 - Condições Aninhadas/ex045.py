# Exercício 45 – GAME: Pedra Papel e Tesoura
# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random

pedra = 1
papel = 2
tesoura = 3

# Sorteio da mão da máquina:
mao_maq = random.randint(1, 3)

print("Vamos jogar Jo Ken Pô?")
mao_jog = int(input("Digite [1] para PEDRA, [2] para PAPEL e [3] para TESOURA: "))

# Exibindo as escolhas:
print(f"\nJogador escolheu: {mao_jog}")
print(f"Máquina escolheu: {mao_maq}")

# Imprimindo o resultado:
if mao_jog == mao_maq:
    print("Empate!")
elif (mao_jog == 1 and mao_maq == 3) or (mao_jog == 2 and mao_maq == 1) or (mao_jog == 3 and mao_maq == 2):
    print("Jogador vence!")
else:
    print("Máquina vence!")

