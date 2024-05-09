C = int(input("Digite o código do operário: "))
N = int(input("Digite o número de horas trabalhadas: "))

if N > 50:
    salario_base = 50 * 10
    
    salario_extra = (N - 50) * 20
    
    salario_total = salario_base + salario_extra
    E = salario_extra
else:
    salario_total = N * 10
    E = 0

print("Salário total:", salario_total)
print("Salário excedente:", E)
