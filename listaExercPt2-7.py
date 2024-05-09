def calcular_area(base, altura):
    return (base * altura) / 2

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

if base > 0 and altura > 0:
    area = calcular_area(base, altura)
    print("A área do triângulo é:", area)
else:
    print("Os valores da base e altura do triângulo devem ser positivos e maiores que zero.")
