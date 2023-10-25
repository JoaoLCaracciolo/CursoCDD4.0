class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} já está falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pois está dormindo")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar pois está comendo")
        else:
            self.falando = True
            print(f"{self.nome} está falando")

    def comer(self,comida):
        if self.falando == True:
            print(f"{self.nome} não pode comer pois está falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer pois está dormindo")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo")
        else:
            self.comendo = True
            print(f"{self.nome} está comendo {comida}")

    def dormir(self):
        if self.falando == True:
            print(f"{self.nome} não está dormindo pois está falando")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")
        elif self.comendo == True:
            print(f"{self.nome} não está dormindo pois está comendo")
        else:
            self.dormindo = True
            print(f"{self.nome} está comendo")

    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
            print("Parou de comer")
        else:
            print("Ele não está comendo")
    def pararDormir(self):
        if self.dormindo == True:
            self.dormindo = False
            print("Acordou")
        else:
            print("Ele não está dormindo")
    def pararFalar(self):
        if self.falando == True:
            self.falando = False
            print("Parou de falar")
        else:
            print("Ele não está Falando")
    def apresentar(self):
        print(f"Olá meu nome é {self.nome} tenho {self.peso}KG e {self.idade} anos")
