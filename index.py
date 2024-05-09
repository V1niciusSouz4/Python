class Conta:
    def __init__(self, numero, saldo, ativo, cpf):
        self.numero = numero
        self.saldo = saldo
        self.ativo = ativo
        self.cpf = cpf 

    def credito(self, valor):
        self.saldo =+ valor

    def debito(self, valor):
        if self.saldo >= valor:
            self =- valor
        else:
            print("Saldo insuficiente!")

    def ativar(self):
        if self.ativo == False:
            self.ativo = True
        else:
            print("Conta já está ativa!")

    def mostrarSaldo(self):
        print(self.saldo)
    
    def __str__(self):
        return self.saldo

class Poupanca(Conta):
        def __init__(self,numero,saldo,ativo,cpf,aniversario):
            super().__init__(numero,saldo,ativo,cpf)

        def atualizar_saldo(self,dia):
            if self.aniversario == dia:
                self.saldo =+ self.saldo * (0.05)
            else: 
                print("tuts tuts")

class Corrente(Conta):
        def __init__(self,numero,saldo,ativo,cpf):
            super().__init__(numero,saldo,ativo,cpf)
        def pedeTalao(self, cheques):
             if(cheques < 3):
                if(saldo >= (cheques*30)):
                    saldo = saldo - (cheques*30)
                else:
                 print('Falha ao requerir cheques, saldo insuficiente!')
             else:
                 print('Falha ao requerir cheques, não há cheques disponpiveis equivalentes ao valor requisitado!')

class Especial(Conta):
    def __init__(self,numero,saldo,ativo,cpf):
            super().__init__(numero,saldo,ativo,cpf)
            self.limite = 1000
    def userLimite(self, valor):
        if(self.saldo <= 0 and (valor < self.limite)):
            self.limite -= valor
        elif(self.limite == 0):
            print('Você não possui limite para executar esta ação')
class Empresa(Conta):
    def __init__(self,numero,saldo,ativo,cpf):
            super().__init__(numero,saldo,ativo,cpf)
            self.emprestimo = 10000
    def userEmpréstimo(self, valor):
        if(valor <= self.emprestimo):
            self.saldo += valor
            self.emprestimo -= valor
        elif(self.limite == 0):
            print('Você não possui saldo de empréstimo para executar esta ação')

class Estudantil(Conta):
    def __init__(self,numero,saldo,ativo,cpf):
            super().__init__(numero,saldo,ativo,cpf)
            self.limiteEstudantil = 5000
    def userEmpréstimo(self, valor):
        if(valor <= self.limiteEstudantil):
            self.saldo += valor
            self.limiteEstudantil += valor
        elif(self.limite == 0):
            print('Você não possui saldo estudantil para executar esta ação')


    
class Conta:
    def __init__(self, numero, saldo, ativo, cpf):
        self.numero = numero
        self.saldo = saldo
        self.ativo = ativo
        self.cpf = cpf 

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def ativar(self):
        if not self.ativo:
            self.ativo = True
        else:
            print("Conta já está ativa!")

    def mostrarSaldo(self):
        print(self.saldo)
    
    def __str__(self):
        return str(self.saldo)

class Poupanca(Conta):
    def __init__(self, numero, saldo, ativo, cpf, aniversario):
        super().__init__(numero, saldo, ativo, cpf)
        self.aniversario = aniversario

    def atualizar_saldo(self, dia):
        if self.aniversario == dia:
            self.saldo += self.saldo * 0.05
        else: 
            print("Tuts tuts")

class Corrente(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)

    def pedeTalao(self, cheques):
        if cheques < 3:
            if self.saldo >= (cheques * 30):
                self.saldo -= cheques * 30
            else:
                print('Falha ao requerir cheques, saldo insuficiente!')
        else:
            print('Falha ao requerir cheques, não há cheques disponíveis equivalentes ao valor requisitado!')

class Especial(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)
        self.limite = 1000

    def userLimite(self, valor):
        if self.saldo <= 0 and (valor < self.limite):
            self.limite -= valor
        elif self.limite == 0:
            print('Você não possui limite para executar esta ação')

class Empresa(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)
        self.emprestimo = 10000

    def userEmpréstimo(self, valor):
        if valor <= self.emprestimo:
            self.saldo += valor
            self.emprestimo -= valor
        elif self.limite == 0:
            print('Você não possui saldo de empréstimo para executar esta ação')

class Estudantil(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)
        self.limiteEstudantil = 5000

    def userEmpréstimo(self, valor):
        if valor <= self.limiteEstudantil:
            self.saldo += valor
            self.limiteEstudantil += valor
        elif self.limite == 0:
            print('Você não possui saldo estudantil para executar esta ação')

def main():

    print("=== Bem-vindo ao Banco da praçan ===")
    print("O banco que cuida do seu dinheiro com segurança e confiança!")
    print()

    tipo_conta = input("Escolha o tipo de conta (Poupança, Corrente, Especial, Empresa, Estudantil): ")
    
    if tipo_conta.lower() == "poupança":
        minha_conta = Poupanca(0, 0, True, None, None)
    elif tipo_conta.lower() == "corrente":
        minha_conta = Corrente(0, 0, True, None)
    elif tipo_conta.lower() == "especial":
        minha_conta = Especial(0, 0, True, None)
    elif tipo_conta.lower() == "empresa":
        minha_conta = Empresa(0, 0, True, None)
    elif tipo_conta.lower() == "estudantil":
        minha_conta = Estudantil(0, 0, True, None)
    else:
        print("Tipo de conta inválido!")
        return

    minha_conta.ativar()

    movimentos = 0
    while movimentos < 10:
        print("\n======= MENU =======")
        print("1. Débito")
        print("2. Crédito")
        print("3. Usar Cheque")
        print("4. Usar Empréstimo")
        print("5. Usar Empréstimo Estudantil")
        print("6. Mostrar Saldo")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para débito: "))
            minha_conta.debito(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para crédito: "))
            minha_conta.credito(valor)
        elif opcao == "3":
            cheques = int(input("Digite o número de cheques a serem emitidos: "))
            minha_conta.pedeTalao(cheques)
        elif opcao == "4":
            valor = float(input("Digite o valor do empréstimo: "))
            minha_conta.userEmpréstimo(valor)
        elif opcao == "5":
            valor = float(input("Digite o valor do empréstimo estudantil: "))
            minha_conta.userEmpréstimo(valor)
        elif opcao == "6":
            minha_conta.mostrarSaldo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

        movimentos += 1

if __name__ == "__main__":
    main()
