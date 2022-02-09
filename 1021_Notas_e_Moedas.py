'''
Leia um valor de ponto flutuante com duas casas decimais. 
Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.
'''
n = input().split('.')
a = int(n[0])
b = int(n[1])
print("NOTAS:")
print("%d nota(s) de R$ 100.00" % (a//100))
a = a % 100
print("%d nota(s) de R$ 50.00" % (a//50))
a = a % 50
print("%d nota(s) de R$ 20.00" % (a//20))
a = a % 20
print("%d nota(s) de R$ 10.00" % (a//10))
a = a % 10
print("%d nota(s) de R$ 5.00" % (a//5))
a = a % 5
print("%d nota(s) de R$ 2.00" % (a//2))
a = a % 2

print("MOEDAS:")
b = b + (a*100)
print("%d moeda(s) de R$ 1.00" % (b//100))
b = b % 100
print("%d moeda(s) de R$ 0.50" % (b//50))
b = b % 50
print("%d moeda(s) de R$ 0.25" % (b//25))
b = b % 25
print("%d moeda(s) de R$ 0.10" % (b//10))
b = b % 10
print("%d moeda(s) de R$ 0.05" % (b//5))
b = b % 5
print("%d moeda(s) de R$ 0.01" % b)