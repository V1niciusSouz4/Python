class Conta:
    def __init__(self, numero, cpf, saldo=0.0):
        self.numero = numero
        self.cpf = cpf
        self._saldo = saldo
        self.ativo = True
        self.limite = 1000.0
        self.cheques_disponiveis = 3
        self.emprestimo_disponivel = 10000.0
        self.emprestimo_estudantil_disponivel = 5000.0

    @property
    def saldo(self):
        return self._saldo

    def ativar(self):
        self.ativo = True

    def debito(self, valor):
        if self.ativo:
            if self.saldo >= valor:
                self._saldo -= valor
            else:
                if self.saldo + self.limite >= valor:
                    self.limite -= valor - self.saldo
                    self._saldo = 0
                else:
                    print("Saldo insuficiente.")
        else:
            print("Conta inativa.")

    def credito(self, valor):
        if self.ativo:
            self._saldo += valor
        else:
            print("Conta inativa.")

    def usar_cheque(self):
        if self.cheques_disponiveis > 0:
            self.cheques_disponiveis -= 1
            self._saldo -= 30.0
        else:
            print("Limite de cheques atingido.")

    def usar_emprestimo(self, valor):
        if valor <= self.emprestimo_disponivel:
            self.emprestimo_disponivel -= valor
            self._saldo += valor
        else:
            print("Limite de empréstimo atingido.")

    def usar_emprestimo_estudantil(self, valor):
        if valor <= self.emprestimo_estudantil_disponivel:
            self.emprestimo_estudantil_disponivel -= valor
            self._saldo += valor
        else:
            print("Limite de empréstimo estudantil atingido.")

print(f"Saldo atual: R${self.saldo}")