'''
Alice e Beatriz colecionam cartas de Pokémon. As cartas são produzidas para um jogo que reproduz a 
batalha introduzida em um dos mais bem sucedidos jogos de videogame da história, mas Alice e Beatriz 
são muito pequenas para jogar, e estão interessadas apenas nas cartas propriamente ditas. Para facilitar, 
vamos considerar que cada carta possui um identificador único, que é um número inteiro.

Cada uma das duas meninas possui um conjunto de cartas e, como a maioria das garotas de sua idade, 
gostam de trocar entre si as cartas que têm. Elas obviamente não têm interesse emtrocar cartas idênticas, 
que ambas possuem, e não querem receber cartas repetidas na troca.Além disso, as cartas serão trocadas em 
uma única operação de troca: Alice dá para Beatriz um sub-conjunto com N cartas distintas e recebe de volta 
um outro sub-conjunto com N cartas distintas.

As meninas querem saber qual é o número máximo de cartas que podem ser trocadas. Por exemplo, se Alice 
tem o conjunto de cartas {1, 1, 2, 3, 5, 7, 8, 8, 9, 15} e Beatriz o conjunto {2, 2, 2, 3, 4, 6, 10, 11, 11}, 
elas podem trocar entre si no máximo quatro cartas. Escreva um programa que, dados os conjuntos de cartas que 
Alice e Beatriz possuem, determine o número máximo de cartas que podem ser trocadas.
'''

while True:
    aux = input()
    if aux == '0 0':
        break
    a, b = set(input().split()), set(input().split())
    ta, tb = 0, 0

    for item in a:
        if item not in b:
            ta += 1
    for item in b:
        if item not in a:
            tb += 1

    print(ta) if ta <= tb else print(tb)