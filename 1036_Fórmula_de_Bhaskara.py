'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.
'''

y = [float(x) for x in input().split()]
a, b, c = y[0], y[1], y[2]

delta = b * b - 4 * a * c

if a != 0 and delta >= 0:
    from math import sqrt    
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print("R1 = " + "%.5f" % x1)
    print("R2 = " + "%.5f" % x2)
else:
    print('Impossivel calcular')