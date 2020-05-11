# numero_certo = 42
#
#
# acertou = False
# while not acertou:
#     chute = int(input("Digite um número para adivinhar: "))
#     acertou = chute == numero_certo
#     maior = chute > numero_certo
#     menor = chute < numero_certo
#     if acertou:
#         print("Acertou")
#     else:
#         if maior:
#             print("O numero secreto é menor")
#         elif menor:
#             print("O numero secreto é maior")
#         else:
#             print("Acertou")

palavra = "abc"
lista = ["_" for i in range(len(palavra))]
print(lista)

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in inteiros if x % 2 == 0]
print(pares)
