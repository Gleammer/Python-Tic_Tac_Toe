#imports all the AI functionality
import numpy as np
import math

maze = np.full((3, 3), '.')

def show_maze(board):
    print("\nThe up-to-date maze is:")
    for i in range(0, 3):
        for j in range(0, 3):
            print(board[i][j], end=' ')
        print()
    print()
    #should make the visualization a bit more comfortable (works for now, might use GUI later)

def get_rank(x, y): #not really necessary
    rez = 0
    if x == y:
        rez += 1
    if x + y == 2:
        rez += 2
    return rez
    """
    this function will return:
    0 - if the pos is on sides
    1 - on the main diagonal
    2 - on the secondary diagonal
    3 - in the center of the matrix
    """

def check_lines(x, y, v):
    if (maze[0][y] == v) and (maze[1][y] == v) and (maze[2][y] == v):
        return 1 #if the winner is found
    if (maze[x][0] == v) and (maze[x][1] == v) and (maze[x][2] == v):
        return 1 #if the winner is found
    return 0

def check_f_diagonal(v):
    if (maze[0][0] == v) and (maze[0][0] == maze[1][1]) and (maze[1][1] == maze[2][2]):
        return True
    return False

def check_s_diagonal(v):
    if (maze[0][2] == v) and (maze[0][2] == maze[1][1]) and (maze[1][1] == maze[2][0]):
        return True
    return False

def check_win(x, y, v):
    if check_lines(x, y, v):
        return 1
    if (x == y) and check_f_diagonal(v):
        return 1
    if (x + y == 2) and check_s_diagonal(v):
        return 1
    return 0

def place(val):
    valid = 0
    while valid == 0:
        x, y = input("At what position do you want to place " + str(val) + "?\n").split()
        x = int(x)
        y = int(y)
        if maze[x][y] != '.':
            print("This cell is already used!")
        else:
            valid = 1
    maze[x][y] = val
    return check_win(x, y, val) #after placing the element it will return whether the winner has been found :)

def start(count): #count==1 for player first and count==-1 for Ai first
    for i in range(0, 9):
        show_maze(maze)
        if count == 1:
            if place('x'):
                print("Player using x has won!")
                return
        else:
            if ai_place('o'):
                print("The AI has won!")
                return
        count *= -1
    print("Frienship has won!")
    pass

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
    return 0 #if nobody has won yet / the game is a tie

def minimax(isMaxim, alpha, beta):
    result = checkWinner()
    space = freeSpaces(maze)
    if result == 0 and space == 0:
        return 0
    elif result > 0:
        return (result * 2 - 3) * (space + 1)
    if isMaxim:
        bestScore = -math.inf
        for i in range(0, 3):
            for j in range(0, 3):
                if maze[i][j] == '.':
                    maze[i][j] = 'o'
                    score = minimax(False, alpha, beta)
                    maze[i][j] = '.'
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return bestScore
    else:
        bestScore = math.inf
        for i in range(0, 3):
            for j in range(0, 3):
                if maze[i][j] == '.':
                    maze[i][j] = 'x'
                    score = minimax(True, alpha, beta)
                    maze[i][j] = '.'
                    bestScore = min(score, bestScore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestScore
    pass

def ai_place(val):
    bestScore = -math.inf
    move = ()
    for i in range(0, 3):
        for j in range(0, 3):
            if maze[i][j] == '.':
                maze[i][j] = val
                score = minimax(False, -math.inf, math.inf)
                maze[i][j] = '.'
                if score > bestScore:
                    bestScore = score
                    move = (i, j)
    maze[move[0]][move[1]] = val
    return check_win(move[0], move[1], val)


#necessary for debugging
def show_ranks():
    for i in range(0, 3):
        for j in range(0, 3):
            print(get_rank(i, j), end=' ')
        print()

#place('x')
#ai_place('o')
#show_maze(maze)
start(1) #for player goes first
#start(-1) #for Ai goes first
