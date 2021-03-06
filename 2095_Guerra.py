'''
Guerra, um evento digno apenas de aparecer na literatura, filmes ou talvez programação de concursos, veio a 
atingir o império Nogloniano, que está enfrentando o império vizinho de Quadradônia. Protocolos de guerra 
combinados por ambas as partes indicam que a guerra será travada em sucessivas batalhas, em cada uma das quais 
um soldado diferente de cada império vai enfrentar outro, de modo que cada soldado irá participar em exatamente 
uma batalha. O império que ganhar mais batalhas ganha a guerra. Cada império tem um exército formado por S soldados, 
e cada soldado tem uma certa habilidade de combate. Em cada batalha entre dois soldados, aquele com maior 
habilidade de combate ganha a batalha. Se ambos os soldados têm as mesmas habilidades de combate, a batalha é 
declarada como empate e tecnicamente nenhum lado é vitorioso. Os espiões de Noglônia tiveram que interceptar 
informações secretas relativas às habilidades de combate de cada soldado do exército de Quadradônia, por isso 
a rainha de Noglônia requer a sua assistência, a fim de calcular o número máximo de batalhas que podem ganhar 
durante a guerra se os seus soldados forem enviados na ordem apropriada.
'''

input()
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])
total = 0

for item_b in b:
    if item_b > a[0]:
        total += 1
        a.remove(a[0])
print(total)