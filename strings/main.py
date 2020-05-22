from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
# url = ""
argumento1 = ExtratorArgumentosUrl(url)
print(argumento1)

argumento2 = ExtratorArgumentosUrl(url)
print(argumento2)

print(argumento1 == argumento2)
# print(id(argumento1), id(argumento2))

print(argumento1 == int(5))

# moeda_origem, moeda_destino = argumento.extrai_argumentos()
# valor = argumento.extrai_valor()
# print(f'{moeda_origem}, {moeda_destino}')
# print(valor)


# string = "bytebankbyte"
# stringNova = string.replace("byte", "mega", 1)
# print(stringNova)

# urlByteBank = "https://bytebank.com"
# url1 = "https://buscasites.com/busca?q=https://bytebank.com"
# url2 = "https://bitebank.com"
# url3 = "https://bytebank.com/cambio/teste/teste"
#
# print(url3.startswith(urlByteBank))

texto = "{serie} é uma excelente série e já possui {temporadas} temporadas"
print(texto.format(serie="Breking bad", temporadas=5))

pizza = "Eu gosto de pizza de {0:>20}".format("Calabresa")
pizza = "Eu gosto de pizza de {0:#>20}".format("Calabresa")
pizza = "Eu gosto de pizza de {0:#^20}".format("Calabresa")
pizza = "Eu gosto de pizza de {0:.5}".format("Calabresa")

file = open("output.txt", "w")
print(pizza, file=file)
