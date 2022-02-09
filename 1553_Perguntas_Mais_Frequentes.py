'''
Muitos sites na internet adicionam uma sessão chamada “Perguntas mais Frequentes” que, como o nome já diz, 
contém as perguntas mais feitas pelos usuários que utilizam o site.

O portal do URI costuma receber muitas perguntas de seus usuários, então Neilor imaginou que seria uma boa 
ideia adicionar uma sessão de Perguntas mais Frequentes no site. Como o Neilor anda muito ocupado ultimamente, 
ele pediu a sua ajuda para adicionar essa sessão.

Dados os identificadores de perguntas feitas pelos usuários, diga o número de perguntas que serão 
adicionadas na nova sessão do site. Uma pergunta é classificada como “frequente” quando ela é feita ao 
menos K vezes.
'''

while True:
    k = input()
    if k == '0 0':
        break
    k = int(k.split()[1])
    total = 0
    aux = [int(x) for x in input().split()]
    for item in set(aux):
        if aux.count(item) >= k:
            total += 1

    print(total)