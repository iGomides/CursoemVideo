# Exercício 14 – Conversor de Temperaturas

"""
Escreva um programa que converta uma temperatura digitando
em graus Celsius e converta para graus Fahrenheit.
"""

c = float(input("Temperatura em graus Célcius: "))
f = (c * 1.8 + 32)
print("A temperatura de {}C corresponde a {:.1f}F.".format(c, f))
