import re

email1 = "meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é meu celular"
email4 = "lalalalalla 993540-12531 iasdawjenmae"

padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"

retorno = re.search(padrao, email4)
print(retorno.group())
