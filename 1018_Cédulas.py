'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor 
pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
A seguir mostre o valor lido e a relação de notas necessárias.
'''

n = int(input())
print(n)
print("%d nota(s) de R$ 100,00" % (n // 100))
n=n % 100
print("%d nota(s) de R$ 50,00" % (n // 50))
n=n % 50
print("%d nota(s) de R$ 20,00" % (n // 20))
n=n % 20
print("%d nota(s) de R$ 10,00" % (n // 10))
n=n % 10
print("%d nota(s) de R$ 5,00" % (n // 5))
n=n % 5
print("%d nota(s) de R$ 2,00" % (n // 2))
n=n % 2
print("%d nota(s) de R$ 1,00" % n)