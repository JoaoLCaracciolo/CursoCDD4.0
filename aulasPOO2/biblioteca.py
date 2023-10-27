class ContaBancaria:

    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0

    def depositar(self, ValorDeposito):
        if ValorDeposito > 0:
            if self.status == True:
                self.saldo += ValorDeposito
            else:
                print("Conta Invalida")
        else:
            print("Valor invalido")

    def sacar(self, ValorSaque):
        if ValorSaque > 0:
            if self.status == True:
                if self.saldo + self.limite < ValorSaque:
                    print("Saldo insuficiente")
                else:
                    if self.saldo < ValorSaque & self.saldo + self.limite > ValorSaque:
                        self.saldo -= ValorSaque
                        print(f"Saque no valor de {ValorSaque} realizado com sucesso")
                    elif self.saldo > ValorSaque:
                        self.saldo -= ValorSaque
                        print(f"Saque no valor de {ValorSaque} realizado com sucesso")
                    else:
                        print("Saldo insuficiente")
            else:
                print("Conta Invalida")
        else:
            print("Valor Invalido")
    def ativarconta(self):
        if self.status == True:
            print("Sua conta já está ativa")
        else:
            self.status = True
            print("Conta Ativada!!")

    def verificarsaldo(self):

        if self.status == True:
            print(f"Seu saldo atual é de R${self.saldo}")
        else:
            print("Conta Invalida")

    def ativarlimite(self, ValorLimite):

        if self.status == True:
            if ValorLimite > 0:
                self.limite += ValorLimite
                print(f"Limite disponivel {ValorLimite}")
            else:
                print("Valor Invalido")
        else:
            print("Conta Invalida")
