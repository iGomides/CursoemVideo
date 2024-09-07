# Exercício 10 – Conversor de Moedas

real = float(input("Informe o valor que você possui em reais: "))
dolar = (real / 5.60)
euro = (real / 6.20)
iene = (real / 0.039)

print("Com esse valor é possível adquirir {:.2f} dólares.".format(dolar))
print("Com esse valor é possível adquirir {:.2f} euros.".format(euro))
print("Com esse valor é possível adquirir {:.2f} ienes.".format(iene))