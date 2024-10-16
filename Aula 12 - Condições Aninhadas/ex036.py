# Exercício 36 – Aprovando Empréstimo

"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.
"""

# Declarando as variáveis
imovel = float(input("Valor do imóvel: "))
salario = float(input("Salário informado: "))
prazo = int(input("Quantidade de parcelas: "))
mensalidade = (imovel / prazo)

# Calculando a aprovação
if mensalidade <= (salario * 0.3):
    print("Empréstimo 'aprovado'.")
else:
    print("Empréstimo 'negado'.")
    print("Motivo: valor da mensalidade ultrapassa 30% da renda mensal do candidato.")
