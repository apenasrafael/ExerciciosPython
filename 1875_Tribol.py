'''
Na cidade de Triangulândia, o maior sonho de sua população era construir um campo de futebol, mas lá todos os 
terrenos são triangulares. Se fosse para fazer um campo retangular, uma boa parte do terreno não seria aproveitada 
para construir o campo. Então, os irmãos Hipo e Tenusa tiveram uma grande ideia: A criação de um novo jogo, 
derivado do futebol, mas jogado em um campo triangular, e chamaram o jogo de Tribol. As regras eram simples:

Jogam três equipes ao mesmo tempo: Red, Green e Blue.

A partida tem um tempo de trinta minutos.
A equipe que fizer um gol no adversário do sentido anti-horário ao mesmo, é um gol normal.
A equipe que fizer um gol no adversário do sentido horário ao mesmo, vale o dobro.
Se as três equipes fizerem a mesma quantidade de gols, ocorre um trempate
Se as duas equipes que fizerem mais gols tiverem feito a mesma quantidade, ocorre um empate, e o jogo é decidido por pênaltis.
A equipe que fizer mais gols, vence.
Exemplo de partida. Os times estão dispostos no campo igual à imagem abaixo.

[IMAGEM]

A equipe Green faz um gol na equipe Blue e um gol na equipe Red, totalizando 3 gols;
A equipe Blue faz dois gols na equipe Green, totalizando 2 gols;
A equipe Red faz dois gols na equipe Green, totalizando 4 gols e vencendo a partida. 

'''

for i in range(int(input())):
    red, green, blue = 0, 0, 0
    for j in range(int(input())):
        gol = input().split()
        marcou, sofreu = gol[0], gol[1]
        if marcou == 'R':
            if sofreu == 'G': red += 2
            else: red += 1
        elif marcou == 'G':
            if sofreu == 'B': green += 2
            else: green += 1
        else:
            if sofreu == 'R': blue += 2
            else: blue += 1

    if red == green == blue:
        print('trempate')
    else:
        lista = [red, green, blue]
        if lista.count(max(lista)) == 2:
            print('empate')
        else:
            if red > blue and red > green:
                print('red')
            elif green > red and green > blue:
                print('green')
            else:
                print('blue')
