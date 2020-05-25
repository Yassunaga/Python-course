# Collections: um conjunto de elementos

idades = [39, 30, 27, 17, 15]
idades.remove(30)

print(idades)

print(28 in idades)
print(15 in idades)

if 15 in idades:
    idades.remove(15)

idades.insert(0, 10)
print(idades)

idades.append([27, 19])
print(idades)

idades = [39, 30, 27, 17, 15]
idades.extend([27, 19])

print(idades)

idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade + 1)

print(idades_ano_que_vem)

idades_ano_que_vem = [i + 1 for i in idades]
print(idades_ano_que_vem)

maiores_de_idade = [idade for idade in idades if idade > 18]
print(maiores_de_idade)


def proximo_ano(idade):
    return idade + 1


idades_ano_que_vem = [proximo_ano(idade) for idade in idades]
print(idades_ano_que_vem)