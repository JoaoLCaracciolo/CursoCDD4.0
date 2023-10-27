class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer")

    def som(self):
        print(f"O {self.nome} está emitindo som")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"O {self.nome} foi miar")

class Cachorro(Animal):

    def __init__(self,nome , cor):
        super().__init__(nome,cor)

    def som(self):
        print(f"O {self.nome} foi latir")

class coelho(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"O {self.nome} foi Ronronar")

class vaca(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"O {self.nome} foi mugir")
