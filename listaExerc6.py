import math

def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def ler_coordenadas():
    x1 = float(input("Digite a coordenada x1: "))
    y1 = float(input("Digite a coordenada y1: "))
    x2 = float(input("Digite a coordenada x2: "))
    y2 = float(input("Digite a coordenada y2: "))
    return x1, y1, x2, y2

def main():
    print("Calculadora de distância entre dois pontos no plano cartesiano")
    x1, y1, x2, y2 = ler_coordenadas()
    distancia = calcular_distancia(x1, y1, x2, y2)
    print(f"A distância entre os pontos é:", distancia)

main()
