'''
O jogo de Sudoku espalhou-se rapidamente por todo o mundo, tornando-se hoje o passatempo mais popular em todo o 
planeta. Muitas pessoas, entretanto, preenchem a matriz de forma incorreta, desrespeitando as restrições do jogo. 
Sua tarefa neste problema é escrever um programa que verifica se uma matriz preenchida é ou não uma solução para 
o problema.

A matriz do jogo é uma matriz de inteiros 9 x 9 . Para ser uma solução do problema, cada linha e coluna deve 
conter todos os números de 1 a 9. Além disso, se dividirmos a matriz em 9 regiões 3 x 3, cada uma destas regiões 
também deve conter os números de 1 a 9. O exemplo abaixo mostra uma matriz que é uma solução do problema.
'''

def eh_linha_valida(board):
    for linha in board:
        if len(set(linha)) != 9:
            return False
    return True

def eh_quadro_valido(cel_row, cel_col):
    vals = board[cel_row][cel_col: cel_col + 3]
    vals.extend(board[cel_row + 1][cel_col: cel_col + 3])
    vals.extend(board[cel_row + 2][cel_col: cel_col + 3])
    return len(set(vals)) == 9

def transforma_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def valida_sudoku():
    if eh_linha_valida(board) and eh_linha_valida(transforma_matriz(board)):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not eh_quadro_valido(i, j):
                    return False
        return True
    else:
        return False

for x in range(int(input())):
    #Ler linhas do Sudoku
    board = list()
    for i in range(9):
        board.append(input().split())
    

    print(f'Instancia {x + 1}')
    print('SIM') if valida_sudoku() else print('NAO')
    print()