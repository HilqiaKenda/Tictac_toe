import numpy as np
import random
from time import sleep


def main_board():
    boards = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])
    return boards

# print(main_board())

def empty_palces(board):
    l=[]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i,j))
    return (l)

# print(empty_palces(boards))

def random_move(board, player):
    select = empty_palces(board)
    current_loc = random.choice(select)
    board[current_loc] = player
    return(board)

# print(random_move(boards, 1))

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x,y] != player:
                win = False
            continue
        if win == True:
            return win
    return win

# print(row_win(boards, 1))

def colum_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y,x] != player:
                win = False
            continue
        if win == True:
            return win
    return win
# print(colum_win(boards, 1))

def diagonal_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x,x] != player:
            win = False
    if win:
        return win
    
    win = True
    if win:
        for y in range(len(board)):
            y = len(board) - 1 - x
            if board[x,y] != player:
                win = False
    return win

# print(diagonal_win(boards, 1))

def evaluate(board):
    winner = 0
    
    for player in [1,2]:
        if (row_win(board, player) or 
        colum_win(board, player) or 
        diagonal_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner -= 1
    return winner

# print(evaluate(boards))

def tic_tac_toe():
    board = main_board()
    winner = 0
    count = 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            brd = random_move(board, player)
            print(f"Board after {count} move")
            print(brd)
            sleep(2)
            count += 1
            winner = evaluate(brd)
        if winner != 0:
            break
    return winner
        # if winner == 0:
        #     break
        # return 'Tie'

print(f"Winner is Playe: {tic_tac_toe()}")