def calcular_media(nota1, nota2, nota3):
    peso1 = .2
    peso2 = .3
    peso3 = .5
    soma_pesos = peso1 + peso2 + peso3
    media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / soma_pesos
    return media

def ler_notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    return nota1, nota2, nota3

def main():
    print("Calculadora de média ponderada")
    nota1, nota2, nota3 = ler_notas()
    media = calcular_media(nota1, nota2, nota3)
    print("A média final é:", media)

main()
