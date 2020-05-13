argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real"


index = argumento.find("=")
print(argumento[index+1:])
