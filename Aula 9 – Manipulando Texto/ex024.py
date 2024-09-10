# Exercício 24 – Verificando as primeiras letras de um texto

"""
Crie um programa que leia o nome de uma cidade diga
se ela começa ou não com o nome “SANTO”.
"""

cidade = str(input("Em qual cidade você mora? ")).title().split()
comeca = (cidade[0] == "Santo")
print("Começa com 'Santo'? {}".format(comeca))
