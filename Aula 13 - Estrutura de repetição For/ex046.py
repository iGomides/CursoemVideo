# Exercício 46 – Contagem regressiva

"""
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

# Importando bibliotecas
from emoji import emojize
from time import sleep

# Declarando o início e o fim da contagem
begin = 10
end = 0

# Declarando a estrutura de repetição
for timer in range(begin, end, -1):
    print(timer)
    sleep(1)
print(emojize('BOOM! ' + ':fireworks: ' * 3))
