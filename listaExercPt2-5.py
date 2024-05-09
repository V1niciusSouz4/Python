indice_poluição = float(input("Digite o índice de poluição medido: "))

if indice_poluição >= 0.5:
    print("Todos os grupos de indústrias devem paralisar suas atividades.")
elif indice_poluição >= 0.4:
    print("Os grupos 1 e 2 de indústrias devem paralisar suas atividades.")
elif indice_poluição >= 0.3:
    print("O grupo 1 de indústrias deve paralisar suas atividades.")
else:
    print("O índice de poluição está dentro dos limites aceitáveis.")
