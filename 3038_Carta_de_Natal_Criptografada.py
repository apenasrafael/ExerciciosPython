'''
O Senhor Claus recebe as mais diversas cartas de crianças do mundo todo. Todo ano, sem exceções, ele seleciona 
algumas das cartas mais legais para dar maior atenção a elas. Neste ano, uma dessas cartas chamou a atenção de 
Claus por um motivo bem peculiar: a carta estava criptografada! Nela, continha a carta com o pedido de natal, 
e um bilhete anexado que dizia o seguinte:

"Sr. Papai Noel: imagino que você deva receber muitas cartas de natal, mas deve ser quase chato ter que ler todas 
elas sem nenhum desafio. Espero que a minha traga um pouco de diversão ao senhor. Eu troquei todas as vogais das 
palavras por símbolos. Use essa tabela para traduzir meu pedido!"
'''

while True:
    try:
        carta = input()
        print(carta.replace('@','a').replace('&','e').replace('!','i').replace('*','o').replace('#','u'))
    except EOFError:
        break