from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
# url = ""
argumento = ExtratorArgumentosUrl(url)
print(argumento)

moeda_origem, moeda_destino = argumento.extrai_argumentos()
valor = argumento.extrai_valor()
print(f'{moeda_origem}, {moeda_destino}')
print(valor)

# string = "bytebankbyte"
# stringNova = string.replace("byte", "mega", 1)
# print(stringNova)

urlByteBank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com"
url3 = "https://bytebank.com/cambio/teste/teste"

print(url3.startswith(urlByteBank))
