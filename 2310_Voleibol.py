'''
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. 
A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques 
cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques 
tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, 
bloqueios e ataques do time todo tiveram sucesso.
'''

saques, bloqueios, ataques = 0, 0, 0
saques_s, bloqueios_s, ataques_s = 0, 0, 0
for i in range(int(input())):
    input()
    total = [int(x) for x in input().split()]
    com_sucesso = [int(x) for x in input().split()]
    saques += total[0]
    bloqueios += total[1]
    ataques += total[2]
    saques_s += com_sucesso[0]
    bloqueios_s += com_sucesso[1]
    ataques_s += com_sucesso[2]

saques = saques_s * 100 / saques
bloqueios = bloqueios_s * 100 / bloqueios
ataques = ataques_s * 100 / ataques

print(f'Pontos de Saque: {saques:.2f} %.')
print(f'Pontos de Bloqueio: {bloqueios:.2f} %.')
print(f'Pontos de Ataque: {ataques:.2f} %.')