'''
Nós temos algumas palavras e queremos justificá-las à direita, ou seja, alinhar todas elas à direita. 
Crie um programa que, após ler várias palavras, reimprima estas palavras com suas linhas justificadas à direita.
'''

palavras = list()
while True:
    x = int(input())
    if x != 0:
        aux = list()
        for i in range(x):
            aux.append(input())
        palavras.append(aux)
    else:
        break

cont = 1
for lista in palavras:
    tam_maior_palavra = len(max(lista, key=len))
    for item in lista:
        print(item.rjust(tam_maior_palavra))
    if cont < len(palavras):
        print()
    cont += 1