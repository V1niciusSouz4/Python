def main():
    banco_nome = "BANCO XYZ - G1"
    banco_slogan = "Aqui ninguém é MIzeravi!"

    print(f"{banco_nome}\n{banco_slogan}\n")

    while True:
        print("MENU PARA SELECIONAR CONTA")
        print("1 - CONTA POUPANÇA")
        print("2 - CONTA CORRENTE")
        print("3 - CONTA ESPECIAL")
        print("4 - CONTA EMPRESA")
        print("5 - CONTA ESTUDANTIL")
        print("6 - SAIR")

        escolha = input("DIGITE O CODIGO DA OPÇÃO SELECIONADA: ")

        if escolha == "1":
            tipo_conta = "POUPANÇA"
            break
        elif escolha == "2":
            tipo_conta = "CORRENTE"
            break
        elif escolha == "3":
            tipo_conta = "ESPECIAL"
            break
        elif escolha == "4":
            tipo_conta = "EMPRESA"
            break
        elif escolha == "5":
            tipo_conta = "ESTUDANTIL"
            break
        elif escolha == "6":
            print("Obrigado por utilizar nossos serviços.")
            return
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    print(f"\nCONTA {tipo_conta}\n")

    

if __name__ == "__main__":
    main()