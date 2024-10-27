# Exercício 49 – Tabuada v.2.0
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número: '))

for contagem in range(1, 11):
    print(f'{numero} x {contagem} = {numero * contagem}')
