'''
Os habitantes do planeta Uno possuem um terrível problema de detecção de números com mais de um algarismo, 
de modo que, para tudo que vão fazer, transformam qualquer valor inteiro em um número de um algarismo, 
realizando somas sucessivas do número até o mesmo ser reduzido a um algarismo. Por exemplo, o número 999999999991, 
no planeta Uno, soma-se todos os algarismos, resultando em 9+9+9+9+9+9+9+9+9+9+9+1 = 100. 
Como o número 100 tem mais de um algarismo, o processo se repete, resultando em 1+0+0 = 1

Uma das grandes dificuldades que os habitantes possuem está em comparar dois números e verificar qual 
deles é o maior, segundo as regras do planeta.

Escreva um programa que, dados dois números inteiros, identifique qual deles é o maior número de um algarismo.
'''


def returnaNumero(num):
    while len(num) > 1:
        num = str(sum([int(x) for x in list(num)]))

    return int(num)

while True:
    aux = input()
    if aux == '0 0':
        break
    aux = aux.split()

    n1, n2 = returnaNumero(aux[0]), returnaNumero(aux[1])

    if n1 > n2:
        print('1')
    elif n1 < n2:
        print('2')
    else:
        print('0')