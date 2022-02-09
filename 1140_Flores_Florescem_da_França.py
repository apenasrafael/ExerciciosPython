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