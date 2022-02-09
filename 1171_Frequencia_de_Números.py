'''
Neste problema sua tarefa será ler vários números e em seguida dizer quantas vezes cada número aparece na 
entrada de dados, ou seja, deve-se escrever cada um dos valores distintos que aparecem na entrada por ordem 
crescente de valor.
'''

l = []
for i in range(int(input())):
    l.append(int(input()))

for item in set(l):
    print(f'{item} aparece {l.count(item)} vez(es)')