'''
Daniela é enfermeira em um grande hospital, e tem os horários de trabalho muito variáveis. 
Para piorar, ela tem sono pesado, e uma grande dificuldade para acordar com relógios despertadores.

Recentemente ela ganhou de presente um relógio digital, com alarme com vários tons, e tem esperança 
que isso resolva o seu problema. No entanto, ela anda muito cansada e quer aproveitar cada momento de descanso. 
Por isso, carrega seu relógio digital despertador para todos os lugares, e sempre que tem um tempo de descanso 
procura dormir, programando o alarme despertador para a hora em que tem que acordar. No entanto, com tanta 
ansiedade para dormir, acaba tendo dificuldades para adormecer e aproveitar o descanso.

Um problema que a tem atormentado na hora de dormir é saber quantos minutos ela teria de sono se adormecesse 
imediatamente e acordasse somente quando o despertador tocasse. Mas ela realmente não é muito boa com números, 
e pediu sua ajuda para escrever um programa que, dada a hora corrente e a hora do alarme, determine o número 
de minutos que ela poderia dormir.
'''

from datetime import datetime

while True:
    aux = input().split()
    if aux == ['0', '0', '0', '0']:
        break
    aux = [int(x) for x in aux]
    h1, m1, h2, m2 = aux[0], aux[1], aux[2], aux[3]
    fmt = '%Y-%m-%d %H:%M:%S'

    day = '02' if h2 < h1 else '01'

    d1 = datetime.strptime(f'2010-01-{day} {h1}:{m1}:00', fmt)
    d2 = datetime.strptime(f'2010-01-{day} {h2}:{m2}:00', fmt)

    diff = int((d2 - d1).seconds / 60)
    print(diff)