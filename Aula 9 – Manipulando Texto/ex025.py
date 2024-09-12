# Exercício 25 – Procurando uma string dentro de outra

"""
Crie um programa que leia o nome de uma pessoa
e diga se ela tem “SILVA” no nome.
"""

nome = str(input("Em qual cidade você mora? ")).title()
print("Possui 'Silva'? {}".format("Silva" in nome))
