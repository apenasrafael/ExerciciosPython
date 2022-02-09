'''
Truco é um jogo de cartas que pode ser jogado por duas ou mais pessoas. Existem diversas variações: o Truco Cego 
ou Truco Espanhol (popular no sul do Brasil, Argentina, Uruguai e outros países), o Truco Paulista, Capixaba 
ou Mineiro (variações populares no Brasil), o Truco Índio e o Truco Eteviano. Em geral, é uma disputa de três 
rodadas (“melhor de três”) para ver quem tem as cartas mais “fortes” (de valor simbólico mais alto).

Adalberto e Bernardete estão jogando uma variação de truco com 40 cartas (foram retirados do baralho todas 
as cartas de valor 8, 9 e 10, além dos coringas), e o valor simbólico independente do naipe da carta. 
A ordem de valor simbólico das cartas nessa variação de truco é mostrada abaixo, ordenada da mais “fraca” 
(mais à esquerda) para a mais “forte” (mais à direita)

4 5 6 7 Q J K A 2 3

Cada partida é disputada em três rodadas. A cada rodada, os jogadores escolhem uma das cartas para mostrar, 
e vence aquele que tiver a carta com o maior valor simbólico. Em caso de empate (ou seja, os dois apresentarem 
cartas com os mesmos valores simbólicos), Adalberto vence, pois é mais velho que Bernardete. Vence a partida 
aquele que vencer o maior número de rodadas.

Depois de algumas partidas, Adalberto e Bernardete estão com dificuldades para saber quem venceu mais partidas, 
e pediram a sua ajuda.

Sua tarefa é escrever um programa que calcule o número de partidas que cada um dos competidores 
(Adalberto e Bernardete) venceram.
'''

a, b = 0, 0
dic = {4: 1, 5: 2, 6: 3, 7: 4, 12: 5, 11: 6, 13: 7, 1: 8, 2: 9, 3: 10}

for i in range(int(input())):
    aux_a, aux_b = 0, 0
    entrada = [int(x) for x in input().split()]
    for i in range(3):
        if dic[entrada[i]] >= dic[entrada[i+3]]:
            aux_a += 1
        else:
            aux_b += 1
        if aux_a == 2 or aux_b == 2:
            break

    if aux_a > aux_b:
        a += 1
    else:
        b += 1

print(f'{a} {b}')