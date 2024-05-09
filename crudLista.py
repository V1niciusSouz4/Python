def adicionar_valor(array):
    while True:
        try:
            valor = int(input("Digite um número inteiro positivo para adicionar ao array (ou digite -1 para sair): "))
            if valor == -1:
                break
            elif valor < 0:
                print("Por favor, digite um número inteiro positivo.")
            else:
                array.append(valor)
                print("Valor adicionado com sucesso ao array!")
        except ValueError:
            print("Por favor, digite um número inteiro positivo válido.")

def excluir_valor(array):
    if len(array) == 0:
        print("O array está vazio.")
        return
    print("Array atual:", array)
    try:
        indice = int(input("Digite o índice do valor a ser excluído: "))
        if 0 <= indice < len(array):
            del array[indice]
            print("Valor excluído com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um índice válido.")

def editar_valor(array):
    if len(array) == 0:
        print("O array está vazio.")
        return
    print("Array atual:", array)
    try:
        indice = int(input("Digite o índice do valor a ser editado: "))
        if 0 <= indice < len(array):
            novo_valor = int(input("Digite o novo valor: "))
            if novo_valor >= 0:
                array[indice] = novo_valor
                print("Valor editado com sucesso!")
            else:
                print("Por favor, digite um número inteiro positivo para o novo valor.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um índice válido.")

def imprimir_array(array):
    print("Array atual:", array)

def main():
    array = []
    while True:
        print("\nMenu:")
        print("1. Adicionar valor")
        print("2. Excluir valor")
        print("3. Editar valor")
        print("4. Imprimir array")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_valor(array)
        elif opcao == '2':
            excluir_valor(array)
        elif opcao == '3':
            editar_valor(array)
        elif opcao == '4':
            imprimir_array(array)
        elif opcao == '5':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
