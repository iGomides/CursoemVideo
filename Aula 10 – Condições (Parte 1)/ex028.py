# Exercício 28 – Jogo da Adivinhação v.1.0

"""
Escreva um programa que faça o computador “pensar” em um
número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O
programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint

aleatorio = randint(0, 5)
chute = int(input('Tente adivinhar um número entre 0 e 5 digitando seu palpite: '))
if chute == aleatorio:
    print("Parabéns, você adivinhou o número!")
else:
    print("Você errou, o número certo era {}.".format(aleatorio))
    print("Tente novamente2 pressionando 'Ctrl + f5'.")
