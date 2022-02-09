'''
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, 
pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em 
benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. 
Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

 _________________________________________________
| RENDA                        | IMPOSTO DE RENDA |
|-------------------------------------------------|
| de 0.00 a R$ 2000.00         | Isento           |
| de R$ 2000.01 até R$ 3000.00 | 8%               |
| de R$ 3000.01 até R$ 4500.00 | 18%              |
| acima de R$ 4500.00          | 28%              |
|_________________________________________________|

'''

salario = float(input())

if salario <= 2000:
    print('Isento')
elif salario <= 3000:
    salario -= 2000
    imposto = 0.08 * salario
    print(f'R$ {imposto:.2f}')
elif salario <= 4500:
    salario -= 3000
    imposto = 80 + (0.18 * salario)
    print(f'R$ {imposto:.2f}')
else:
    salario -= 4500
    imposto = 350 + (0.28 * salario)
    print(f'R$ {imposto:.2f}')