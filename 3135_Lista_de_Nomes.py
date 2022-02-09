'''
Marta quer escolher alguns nomes para o seu futuro filho ou filha. Ela encontrou uma lista de nomes, 
mas não gostou da forma que está apresentada. Ela queria ter uma lista de nomes, onde cada linha estivesse 
ordenada de acordo com o tamanho do nome, do menor para o maior. Em cada linha, irá aparecer apenas um nome 
de um dado tamanho. Por exemplo, considere uma lista com os nomes Eva e Ana. Na apresentação proposta, 
Eva irá aparecer na primeira linha enquanto Ana na segunda.

Que tal fazermos um algoritmo que produz essa lista de nomes?
'''

x = int(input())
nomes = list()
dic = {}
nomes_agrupados = list()

for i in range(x):
  nomes.append(input())

for nome in nomes:
  if len(nome) not in dic.keys():
    dic[len(nome)] = 1
  else:
    dic[len(nome)] += 1

for item in sorted(dic.keys()):
  nomes_agrupados.append(list(filter(lambda nome: len(nome) == item, nomes)))

aux = ''
cont = 0
while cont < len(nomes):
  for grupo in nomes_agrupados:
    if len(grupo) > 0:
      aux += grupo[0] + ', '
      grupo.remove(grupo[0])
      cont += 1

  print(aux[:len(aux)-2])
  aux = ''