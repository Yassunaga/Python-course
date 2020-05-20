from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
# url = ""
argumento = ExtratorArgumentosUrl(url)
print(argumento)

print(ExtratorArgumentosUrl.is_url_valida(url))
moeda_origem, moeda_destino = argumento.extrai_argumentos()
valor = argumento.extrai_valor()
print(f'{moeda_origem}, {moeda_destino}')
print(valor)

# string = "bytebankbyte"
# stringNova = string.replace("byte", "mega", 1)
# print(stringNova)

