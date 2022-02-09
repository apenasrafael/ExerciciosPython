'''
Você começou a competir com seu amigo para ver quem consegue ler mais livros em menos tempo. 
Seu amigo lia muito mais que você, até o dia que você percebeu que ele lia somente livros muito finos.

Então você resolveu contar as páginas dos livros, aumentando também a quantidade de páginas lidas por dia. 
Agora você lê 5 páginas por dia e termina 16 dias antes do que se estivesse lendo 3 páginas por dia. 
Neste cenário, quantas páginas tem o livro?
'''

while True:
    aux = input().split()
    if aux == ['0']:
        break
    a, b, c = int(aux[0]), int(aux[1]), int(aux[2])
    x = (a * b * c) / (c - a)
    if x < 2:
        print('1 pagina')
    else:
        print(f'{int(x):.0f} paginas')