def calcular_quadrado(numero):
    return numero ** 2

numeros = []
for i in range(4):
    numero = float(input("Digite o {}º número: ".format(i + 1)))
    numeros.append(numero)

quadrados = [calcular_quadrado(numero) for numero in numeros]

if quadrados[2] >= 1000:
    print("O quadrado do terceiro número é maior ou igual a 1000: {}".format(quadrados[2]))
else:
    print("Valores lidos e seus respectivos quadrados:")
    for i in range(4):
        print("Número:", numeros[i], "- Quadrado:", quadrados[i])
