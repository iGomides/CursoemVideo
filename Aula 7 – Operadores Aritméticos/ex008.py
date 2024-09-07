# Exercício 8 – Conversor de Medidas

m = float(input("Informe uma medida em metros: "))

km = (m / 1000)
hm = (m / 100)
dam = (m / 10)
dm = int(m * 10)
cm = int(m * 100)
mm = int(m * 1000)

print("A medida de {}m corresponde a: ")
print(km, "km")
print(hm, "hm")
print(dam, "dam")
print(dm, "dm")
print(cm, "cm")
print(mm, "mm")