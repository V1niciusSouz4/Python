idade = int(input("Digite a idade do nadador: "))

categorias = {
    (5, 7): "Infantil A",
    (8, 11): "Infantil B",
    (12, 13): "Juvenil A",
    (14, 17): "Juvenil B",
    (18, float('inf')): "Adultos"
}

categoria_nadador = None
for faixa_etaria, categoria in categorias.items():
    if idade >= faixa_etaria[0] and idade <= faixa_etaria[1]:
        categoria_nadador = categoria
        break

if categoria_nadador:
    print("O nadador está na categoria", categoria_nadador)
else:
    print("Não foi possível determinar a categoria do nadador.")
