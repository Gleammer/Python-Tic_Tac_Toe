import numpy as np
#imports all the AI functionality
from minimax import *

maze = np.full((3, 3), '.')

def show_maze(board):
    print("\nThe up-to-date maze is:")
    for i in range(0, 3):
        for j in range(0, 3):
            print(board[i][j], end=' ')
        print()
    print()
    #should make the visualization a bit more comfortable (works for now, might use GUI later)

def get_rank(x, y):
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
    for i in range(0, 3):
        if maze[i][i] != v:
            return 0
    return 1 #if the winner is found

def check_s_diagonal(v):
    for i in range(0,3):
        if maze[i][2-i] != v:
            return 0
    return 1 #if the winner is found

def check_win(x, y, v):
    rank = get_rank(x, y)
    if check_lines(x, y, v):
        return 1
    if (rank == 1) and check_f_diagonal(v):
        return 1
    elif (rank == 2) and check_s_diagonal(v):
        return 1
    elif (rank == 3) and (check_f_diagonal(v) or check_s_diagonal(v)):
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
            if ai_place(maze, 'o'):
                print("The AI has won!")
                return
        count *= -1
    print("Frienship has won!")
    pass

#necessary for debugging
def show_ranks():
    for i in range(0, 3):
        for j in range(0, 3):
            print(get_rank(i, j), end=' ')
        print()

def test():
    x, y = input("wassap wigga?!").split()
    print(x, " and ", y, " make:", int(x) + int(y))

start(1) #for player goes first
#start(-1) for Ai goes first

#show_ranks()
#place(1)
#show_maze()
#test()
