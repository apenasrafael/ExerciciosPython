'''
O sorteio das posições dos jogadores na chave decisiva da copa do mundo de ping-pong está deixando a todos 
nervosos. É que ninguém quer pegar o jogador mais bem ranqueado, o Master Kung, logo nas oitavas de final, 
ou nas quartas de final. Melhor que só seja possível enfrentar Master Kung na semifinal ou na final! 
Os jogadores são identificados por números inteiros de 1 a 16, sendo que Master Kung é o jogador de número 1. 
O jogador para o qual nós estamos torcendo, Master Lu, tem o número 9.

A chave possui 16 posições também numeradas de 1 a 16, como na figura abaixo. A organização da copa vai fazer um 
sorteio para definir em qual posição cada jogador vai iniciar a chave decisiva. Nas oitavas de final, o jogador 
na posição 1 enfrenta o jogador na posição 2; o da posição 3 enfrenta o da posição 4; e assim por diante, como 
na figura.

[figura]

O objetivo deste problema é decidir em que fase da chave os jogadores Master Kung e Master Lu vão se enfrentar, 
caso vençam todas as suas respectivas partidas antes de se enfrentarem. Por exemplo, se o sorteio da chave 
determinar a seguinte ordem de jogadores da posição 1 até a 16: [4, 11, 3, 2, 8, 13, 14, 5, 16, 9, 12, 6, 10, 7, 1, 15], 
eles vão se enfrentar na semifinal.

'''

dicionario = {3: 'oitavas', 2: 'quartas', 1: 'semifinal', 0: 'final'}

aux = [int(x) for x in input().split()]

for i in range(4):
    limite = len(aux) // 2
    if (1 in aux[:limite] and 9 in aux[limite:]) or (9 in aux[:limite] and 1 in aux[limite:]):
        print(dicionario[i])
        break
    else:
        if 1 in aux[:limite]:
            aux = aux[:limite]
        else:
            aux = aux[limite:]
