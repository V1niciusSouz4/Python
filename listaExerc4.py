import math

try:
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    R = (a + b) ** 2
    S = math.pow((b + c), 2)
    D = (R + S) / 2

    print(f"O valor de D = {D:.2f}")
except ValueError:
    print("Você não digitou um valor inteiro válido.")
print('Fim do programa')
