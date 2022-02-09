'''
Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar 
mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo 
o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições 
para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim 
sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer 
caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. 
Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá 
produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. 
Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.
'''

from string import ascii_lowercase, ascii_uppercase

n = int(input())
for i in range(n):
    p = ''
    word = input()
    for letter in word:
        if letter in ascii_lowercase or letter in ascii_uppercase:
            p += chr(ord(letter) + 3)
        else:
            p += letter
    p = p[::-1]
    aux = ''
    for j in range(len(p) // 2, len(p)):
        aux += chr(ord(p[j]) - 1)

    print(p[:len(p) // 2] + aux)