'''
Joãozinho tem que ajudar seu pai. Um relatório específico com alguns números está saindo com caracteres 
indesejáveis no meio. A ideia é apenas somar os 3 valores que aparecem em cada linha sempre na mesma posição, 
ignorando as letras e apresentar esta soma. Não existem espaços em branco na linha.
'''

from string import ascii_lowercase

for i in range(int(input())):
    entrada = input().lower()
    aux = ''
    for item in entrada:
        if item in ascii_lowercase:
            aux += ' '
        else:
            aux += item
    total = sum([int(x) for x in aux.split()])
    print(total)