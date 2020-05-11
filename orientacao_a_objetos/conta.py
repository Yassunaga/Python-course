class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print(self.__saldo)

    def printa_atributos(self):
        b = [i for i in dir(self) if not i.startswith("__")]
        print(b)


conta = Conta(1,"Gabriel", 120, 1000)

conta.qwe = 100
conta.printa_atributos()

