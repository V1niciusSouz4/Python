def calcular_custo_ao_consumidor(custo_fabrica):
    percentagem_distribuidor = 0.28
    percentagem_impostos = 0.45
    
    custo_distribuidor = custo_fabrica * percentagem_distribuidor
    custo_impostos = custo_fabrica * percentagem_impostos
    custo_total = custo_fabrica + custo_distribuidor + custo_impostos
    
    return custo_total

def main():
    custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
    
    custo_consumidor = calcular_custo_ao_consumidor(custo_fabrica)
    
    print("O custo ao consumidor do carro é:", custo_consumidor)

main()
