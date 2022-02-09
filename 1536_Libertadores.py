'''
A Copa Libertadores da América é a principal competição de futebol entre clubes profissionais da América do Sul, 
organizada pela Confederação Sul-Americana de Futebol (CONMEBOL). Ela é conhecida por ter um regulamento muito 
complicado, principalmente nas fases das oitavas, quartas e semi-final.

Nessas fases são jogadas partidas de ida e volta no sistema mata-mata. Ganha quem fizer a maior pontuação no 
acumulado das duas partidas, sendo 3 pontos para vitória e 1 ponto em caso de empate, ambos por partida. 
Em caso de igualdade na pontuação, são critérios de desempate:

1) saldo de gols (número de gols a favor menos o número de gols contra).

2) mais gols marcados na casa do adversário.

3) disputa por pênaltis.

Todos os critérios devem ser aplicados considerando o acumulado das duas partidas.

Será que você consegue elaborar um algoritmo que, dados os resultados das partidas de ida e de volta, ele 
identifica o time vencedor?
'''

class Time:
    def __init__(self, pontos=0, saldo=0):
        self.pontos = pontos
        self.saldo = saldo

for i in range(int(input())):
    j1, j2 = input().split(), input().split()

    if j1 == j2:
        print('Penaltis')
    else:
        j1.remove('x'), j2.remove('x')
        j1, j2 = [int(x) for x in j1], [int(x) for x in j2]
        t1 = Time()
        t2 = Time()

        if j1[0] > j1[1]:
            t1.pontos += 3
        elif j1[1] > j1[0]:
            t2.pontos += 3

        if j2[0] > j2[1]:
            t2.pontos += 3
        elif j2[1] > j2[0]:
            t1.pontos += 3

        if t1.pontos > t2.pontos:
            print('Time 1')
        elif t1.pontos < t2.pontos:
            print('Time 2')
        else:
            t1.saldo = j1[0] - j1[1] + j2[1] - j2[0]
            t2.saldo = j1[1] - j1[0] + j2[0] - j2[1]

            if t1.saldo > t2.saldo:
                print('Time 1')
            elif t1.saldo < t2.saldo:
                print('Time 2')
            else:            
                print('Time 1') if j2[1] > j1[1] else print('Time 2')
