# Exercício 47 – Contagem de pares
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

inicio = 1
fim = 50

for contagem in range(inicio, fim, 2):
    print(contagem + 1, end=' ')
print('Acabou')