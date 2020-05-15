from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
# url = ""
argumento = ExtratorArgumentosUrl(url)
print(argumento)

print(ExtratorArgumentosUrl.is_url_valida(url))
moeda_origem, moeda_destino = argumento.extrai_argumentos()
print(f'{moeda_origem}, {moeda_destino}')

