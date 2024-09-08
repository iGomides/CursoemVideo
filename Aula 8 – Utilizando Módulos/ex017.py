# Exercício 17 – Catetos e Hipotenusa

"""
Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
cateto_oposto = float(input("Qual o valor do cateto oposto? "))
cateto_adjacente = float(input("Qual o valor do cateto adjacente? "))
hipotenusa_quadrado = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = (hipotenusa_quadrado ** 0.5)

print("O valor da hipotenusa é {:.2f}.".format(hipotenusa))
