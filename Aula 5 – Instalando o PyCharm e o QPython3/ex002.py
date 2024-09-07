# Exercício 2 – Respondendo ao Usuário

'''
Faça um programa que leia o nome de uma pessoa
e mostre uma mensagem de boas-vindas.
'''

nome = str(input('Digite seu nome: ')).strip().title()
print("Muito prazer em te conhecer, {}.".format(nome))
