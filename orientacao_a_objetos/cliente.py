from typing import Final


class Cliente:

    PI: Final[float] = 3.14

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nomes(self):
        return self.__nome.title()

    @nomes.getter
    def nome(self, nome):
        if len(nome) < 3:
            print("O nome deve ter mais de 3 letras!")
            return
        self.__nome = nome
