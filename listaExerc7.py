def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d
    if determinante == 0:
        return None  
    
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)
    return x, y

def ler_coeficientes():
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    d = float(input("Digite o coeficiente d: "))
    e = float(input("Digite o coeficiente e: "))
    f = float(input("Digite o coeficiente f: "))
    return a, b, c, d, e, f

def main():
    print("Calculadora de sistema de equações lineares")
    a, b, c, d, e, f = ler_coeficientes()
    solucao = resolver_sistema(a, b, c, d, e, f)
    if solucao is not None:
        x, y = solucao
        print("Solução para o sistema:")
        print("x =", x)
        print("y =", y)
    else:
        print("O sistema não tem solução.")

main()
