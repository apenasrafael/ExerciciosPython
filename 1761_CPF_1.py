'''
Você foi contratado pelas Indústrias Udilandenses (INUDIL) para desenvolver uma maneira de verificar se o 
Cadastro de Pessoa Física (CPF) indicado por um cliente era válido ou não. Conversando com amigos, você 
chegou à conclusão de que um CPF seria válido se a soma de todos os seus dígitos resultasse em número 
múltiplo de 11. Após verificação minuciosa, você descobriu que essa maneira só funciona em cerca de 80% dos casos, 
e você precisa de mais do que isso para garantir a qualidade do seu trabalho. Após pesquisar mais, você 
descobriu que dos 11 dígitos do CPF, os dois últimos são verificadores e dependem dos 9 dígitos anteriores. 
Vamos introduzir alguma notação. Considere um CPF com os seguintes dígitos

a1a2a3.a4a5a6.a7a8a9-b1b2

Para descobrirmos o dígito b1, procedemos da seguinte maneira: multiplicamos o primeiro por 1, o segundo por 2, 
o terceiro por 3, o quarto por 4 e vamos assim até multiplicarmos o nono por 9. Então, somamos tudo isto. 
Após termos somado tudo, dividimos por 11. O dígito b1 será o resto da divisão (ou 0, caso o resto seja 10).

Para o segundo dígito verificador, temos o seguinte: multiplicamos o primeiro por 9, o segundo por 8, o terceiro 
por 7, o quarto por 6 e vamos assim até multiplicarmos o nono por 1. Então, somamos tudo isto e dividimos por 11. 
O dígito b2 será o resto da divisão (ou 0, caso o resto seja 10).

Sabendo que isso vale para 100% dos CPFs, sua missão é implementar um programa que, dado um CPF, diga se ele é 
válido ou não.
'''

while True:
    try:
        aux = list(int(x) for x in input().replace('.','').replace('-',''))
        b1 = b2 = 0
        b2_pos = 9
        for i in range(9):
            b1 += aux[i] * (i+1)
            b2 += aux[i] * b2_pos
            b2_pos -= 1

        resto_b1 = b1 % 11
        resto_b2 = b2 % 11
        if resto_b1 == 10:
            resto_b1 = 0
        if resto_b2 == 10:
            resto_b2 = 0

        if aux[9] == resto_b1 and aux[10] == resto_b2:
            print('CPF valido')
        else:
            print('CPF invalido')

    except EOFError:
        break