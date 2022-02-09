'''
Mangojata está aprendendo programação. Ela acha tudo muito fácil, muito simples. 
Ela está prestes a fazer um pequeno programa que leia o nome dos seus amigos e a distância de 
sua casa até cada um deles. Desta forma, ela quer simplesmente calcular qual é a distância média 
que deve ser percorrida para chegar na casa de qualquer um de seus amigos (em metros). 
Porém Aristoclenes, que é um programador mais experiente, lhe alertou que às vezes o que parece 
muito simples tem lá seus detalhes, dependendo da linguagem que é utilizada para implementação.
'''

distancia = amigos = 0

while True:
    try:
        input()
        amigos += 1
        distancia += float(input())

    except EOFError:
        print(f'{(distancia/amigos):.1f}')
        break