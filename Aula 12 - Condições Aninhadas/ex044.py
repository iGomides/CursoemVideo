# Exercício 44 – Gerenciador de Pagamentos

"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

    • À vista dinheiro/cheque: 10% de desconto
    • À vista no cartão: 5% de desconto
    • Em até 2x no cartão: preço formal
    • Em 3x ou mais no cartão: 20% de juros
"""

# Recebendo a entrada do valor do produto
preco = float(input("Informe o valor do produto: R$: "))

print("\nSelecione a forma de pagamento:")
print("OPÇÃO [1]: À vista (dinheiro/cheque) -- 10% de desconto")
print("OPÇÃO [2]: À vista (cartão) -- 5% de desconto")
print("OPÇÃO [3]: Em até 2x no cartão -- Sem desconto")
print("OPÇÃO [4]: 3x ou mais no cartão -- 20% de juros")

pagamento = input("\nDigite [1], [2], [3] ou [4]: ")

if pagamento == "1":
    valor_final = preco * 0.9
    print(f"\nValor final com 10% de desconto: R$ {valor_final:.2f}")
elif pagamento == "2":
    valor_final = preco * 0.95
    print(f"\nValor final com 5% de desconto: R$ {valor_final:.2f}")
elif pagamento == "3":
    print(f"\nValor final: R$ {preco:.2f}")
elif pagamento == "4":
    valor_final = preco * 1.2
    print(f"\nValor final com 20% de juros: R$ {valor_final:.2f}")
else:
    print("\nOpção inválida. Tente novamente.")
