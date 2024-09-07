# Exercício 11 – Pintando Parede

'''
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2 metros quadrados.
'''

altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))
metragem = (altura * largura)
tinta = (metragem / 2)

print("A parede possui {:.1f}m². Será necessário {:.1f}l de tinta para pinta-la.".format(metragem, tinta))
