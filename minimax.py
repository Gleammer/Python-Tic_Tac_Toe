#imports all the basic functionality
from TicTacToe import *
import math

def isFull(board):
    for i in range(0,3):
        for j in range(0, 3):
            if board[i][j] == '.':
                return False #because it found a free spot
    return True #because it found no free spots == isFull

def freeSpaces(board):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                count += 1
    return count #returns the number of free spaces

def checkWinner():
    for i in range(0, 3):
        if check_win(i, i, 'x'):
            return 1 #if the player has won
        if check_win(i, i, 'o'):
            return 2 #if the AI has won
    return 0

def minimax(board, isMaxim):


    pass

def bestMove():
    bestScore = -math.inf

def ai_place(board, val):

    pass

temp = maze
temp[2][0] = 'x'
temp[1][1] = 'x'
temp[0][2] = 'x'
