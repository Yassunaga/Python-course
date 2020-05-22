import re

email1 = "meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é meu celular"
email4 = "lalalalalla 99543-1253 iasdawjenmae 9876-1234 912345674"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"
padrao2 = "[0-9]{4,5}-?[0-9]{4}"

# re.search procura pela primeira ocorrência
# re.findall busca todas as ocorrências
# retorno = re.findall(padrao, email4)
# print(retorno)

padrao_data_hora = "[a-z]{5,7} [0-9]{2}h"
frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"

retorno = re.findall(padrao_data_hora, frase3)
print(retorno)
