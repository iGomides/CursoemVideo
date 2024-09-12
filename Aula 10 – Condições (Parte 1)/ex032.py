# Exercício 32 – Ano Bissexto
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


ano_atual = int(input("Digite o ano atual: "))
divisor = 4
resto = ano_atual % divisor

if resto == 0:
    print("Estamos em um ano bissexto!")
else:
    print("Não estamos em um ano bissexto!")
    if resto + 1 ==4:
        print(f"O próximo ano bissexto será {ano_atual + 1}.")
    if resto + 2 ==4:
        print(f"O próximo ano bissexto será {ano_atual + 2}.")
    if resto + 3 == 4:
        print(f"O próximo ano bissexto será {ano_atual + 3}.")
