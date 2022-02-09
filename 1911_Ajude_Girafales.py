'''
Minutos antes do término das aulas, professor Girafales passa uma lista de presença. Certo dia, ele resolveu 
conferir as assinaturas e notou que alguns alunos assinavam diferente em algumas aulas e desconfiou que alguém 
poderia estar assinando por eles. Como o professor possui muitos alunos e pouco tempo (o café com dona Florinda 
é prioridade), ele pediu sua ajuda para validar as assinaturas. Uma assinatura é considerada falsa se houver 
mais de uma diferença entre a original e a que estiver sendo checada. Considere diferença uma troca de maiúscula 
para minúscula ou o contrário.
'''

while True:
    n = input()
    if n == '0': break
    dic = {}
    assinaturas_falsas = 0
    for i in range(int(n)):
        aux = input().split()
        dic[aux[0]] = aux[1]
    for i in range(int(input())):
        erros = 0
        aux = input().split()
        nome = aux[0]
        assinatura_na_aula = aux[1]
        for j in range(len(dic[nome])):
            if dic[nome][j] != assinatura_na_aula[j]:
                erros += 1
            if erros > 1:
                assinaturas_falsas += 1
                break
    print(assinaturas_falsas)