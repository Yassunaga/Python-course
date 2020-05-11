import random

erros = 0

acertou = False
enforcou = False

palavra = "banana"
forca = ["_" for letra in palavra]


def inicia_forca(palavra):
    return ["_" for letra in palavra]


inicia_forca(palavra)
palavras = []
with open("frutas.txt", "r") as arquivo:
    for fruta in arquivo:
        palavras.append(fruta.strip())
palavra = palavras[random.randrange(len(palavras))]
print(palavra)

while not acertou and not enforcou:
    chute = str(input("Tente uma letra: "))
    print("Restam {} tentativas".format(5-erros))
    if chute.upper() in palavra.upper():
        for index, letra in enumerate(palavra):
            if letra.upper() == chute.upper():
                forca[index] = letra
        print(forca)
        acertou = "_" not in forca
        if acertou:
            print("GANHOU !!!")
    else:
        erros += 1

    enforcou = erros == 6
    if enforcou:
        print("ENFORCOU !!!")
