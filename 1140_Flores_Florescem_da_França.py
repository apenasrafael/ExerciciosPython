'''
Fiona sempre amou poesia, e recentemente descobriu uma forma poética fascinante. Tautogramas são um caso especial de aliteração, que é a ocorrência da 
mesma letra no início de palavras adjacentes. Em particular, uma sentença é um tautograma se todas suas palavras começam com a mesma letra.

Por exemplo, as seguintes sentenças são tautogramas:
> Flowers Flourish from France
> Sam Simmonds speaks softly
> Peter pIckEd pePPers
> truly tautograms triumph
> Fiona quer deslumbrar seu namorado com uma carta romântica repleta desse tipo de sentenças. Por favor, ajude Fiona a verificar se cada sentença 
que ela escreveu é um tautograma ou não.
'''


while True:
    sentence = input().lower().split()

    if sentence == ['*']:
        break

    c, yes = sentence[0][0], True

    for i in range(1, len(sentence)):
        if sentence[i][0] != c:
            yes = False
            break

    print('Y') if yes else print('N')
