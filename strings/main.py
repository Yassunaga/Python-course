from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar"
# url = ""
argumento = ExtratorArgumentosUrl(url)
print(argumento)

print(ExtratorArgumentosUrl.is_url_valida(url))
moeda_origem, moeda_destino = argumento.extrai_argumentos()
print(f'{moeda_origem}, {moeda_destino}')

# string = "bytebankbyte"
# stringNova = string.replace("byte", "mega", 1)
# print(stringNova)

