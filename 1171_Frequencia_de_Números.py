'''
Neste problema sua tarefa será ler vários números e em seguida dizer quantas vezes cada número aparece na 
entrada de dados, ou seja, deve-se escrever cada um dos valores distintos que aparecem na entrada por ordem 
crescente de valor.
'''

dicionario = dict()
for i in range(int(input())):
    numero = int(input())
    if numero not in dicionario.keys():
        dicionario[numero] = 1
    else:
        dicionario[numero] += 1
    
for item in sorted(dicionario.keys()):
    print(f'{item} aparece {dicionario[item]} vez(es)')
