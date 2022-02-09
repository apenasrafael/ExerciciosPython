'''
Dona Clotilde é uma senhora muito simpática que mora em uma vila, na casa 71. Não se sabe ao certo por que, mas tinha fama de ser bruxa. Clotilde tinha muita 
vontade de assistir uma partida de futebol. Certo dia, ela comprou um líquido para limpar prata e com isto, ganhou um cupom que dava direito a concorrer a um 
ingresso para a semifinal da copa do mundo de 2014, no Mineirão, o jogo entre Alemanha x Brasil. O sorteio veio e ela ganhou o ingresso. Clotilde foi ao jogo, 
o Brasil perdeu de 7 x 1, e todos da vila acharam que o Brasil tinha perdido daquela forma por causa dela, coitada! O sobrinho hacker dela, San Tanaz, tomando 
as dores da tia, resolveu criar um vírus de computador que interferisse em cálculos matemáticos, de modo que, tudo que envolvesse o número 7 nas contas, se 
tornaria 0.

Por exemplo:
3 + 4 = 0
33 + 44 = 0
17 + 11 = 21
8 x 9 = 2
12 x 7 = 0
8 + 9 = 10
'''

aux = input().split()
aux[0] = int(aux[0].replace('7', '0'))
aux[2] = int(aux[2].replace('7', '0'))

if aux[1] == '+':
    print(int(str(aux[0] + aux[2]).replace('7', '0')))
else:
    print(int(str(aux[0] * aux[2]).replace('7', '0')))
