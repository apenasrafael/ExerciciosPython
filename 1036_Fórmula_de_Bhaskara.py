'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.
'''

from math import sqrt

a, b, c = [float(x) for x in input().split()]
delta = b * b - 4 * a * c

if a != 0 and delta >= 0:    
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)    
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
else:
    print('Impossivel calcular')
