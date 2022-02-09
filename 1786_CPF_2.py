'''
As Indústrias Udilandenses (INUDIL) precisam outra vez de sua ajuda! Depois de criar um programa que verifica 
se um CPF é válido ou não, agora querem que você crie um programa que exiba o CPF do cliente conhecendo apenas 
os 9 primeiros dígitos. O setor de Recursos Humanos gentilmente te informou como funciona um CPF:

Dos 11 dígitos do CPF, os dois últimos são verificadores e dependem dos 9 dígitos anteriores. Vamos introduzir 
alguma notação. Considere um CPF com os seguintes dígitos

a1 a2 a3 . a4 a5 a6 . a7 a8 a9 - b1 b2

Para descobrirmos o dígito b1, procedemos da seguinte maneira:

MUltiplicamos o primeiro por 1, o segundo por 2, o terceiro por 3, o quarto por 4 e vamos assim até multiplicarmos 
o nono por 9. Então, somamos tudo isto. Após termos somado tudo, dividimos por 11. O dígito b1 será o resto da 
divisão (ou 0, caso o resto seja 10).

Para o segundo dígito verificador, temos o seguinte:

Multiplicamos o primeiro por 9, o segundo por 8, o terceiro por 7, o quarto por 6 e vamos assim até multiplicarmos 
o nono por 1. Então, somamos tudo isto e dividimos por 11. O dígito b2 será o resto da divisão (ou 0, caso o 
resto seja 10).

'''

while True:
    try:
        cpf = [int(x) for x in list(input())]
        b2_mult = 9
        b1 = b2 = 0

        for i in range(9):
            b1 += cpf[i] * (i+1)
            b2 += cpf[i] * b2_mult
            b2_mult -= 1

        b1 = b1 % 11
        b2 = b2 % 11
        b1 = 0 if b1 == 10 else b1
        b2 = 0 if b2 == 10 else b2

        cpf = ''.join([str(x) for x in cpf])
        print(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}-{b1}{b2}')

    except EOFError:
        break