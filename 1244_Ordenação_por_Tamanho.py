'''
Crie um programa para ordenar um conjunto de strings pelo seu tamanho. Seu programa deve receber um conjunto 
de strings e retornar este mesmo conjunto ordenado pelo tamanho das palavras, se o tamanho das strings for 
igual, deve-se manter a ordem original do conjunto.
'''

for i in range(int(input())):
    dic = {}
    aux = ''
    frase = input().split()
    for palavra in frase:
        size = len(palavra)
        if size not in dic.keys():
            dic[size] = [palavra]
        else:
            dic[size] += [palavra]

    for i in sorted(dic.keys())[::-1]:
        aux += ' '.join(dic[i]) + ' '
    print(aux[:-1])