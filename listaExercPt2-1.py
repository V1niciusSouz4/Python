P = float(input("Digite o peso dos tomates em quilos: "))

if P > 50:
    E = P - 50
    M = E * 4
else:
    E = 0
    M = 0
print("Excesso:", E, "quilos")
print("Multa a pagar: R$", M)
