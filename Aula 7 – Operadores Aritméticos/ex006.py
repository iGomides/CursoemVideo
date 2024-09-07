# Exercício 6 – Dobro, Triplo, Raiz Quadrada

'''
Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.
'''


num = int(input("Digite um número: "))
dob = (num * 2)
tri = (num * 3)
sqr = (num ** (1/2))

print("O dobro de {} é {}, o triplo é {} e a raiz é {}.".format(num, dob, tri, sqr))
