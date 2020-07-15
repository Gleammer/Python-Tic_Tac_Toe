import numpy as np

maze = np.full((3, 3), '.')
g_rez = 0

def show_maze():
    print(maze)
    #should make the visualization a bit more comfortable

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

def start():
    for i in range(0, 9):
        iasdasasdjklasb
    pass

#necessary for debugging
def show_ranks():
    for i in range(0, 3):
        for j in range(0, 3):
            print(get_rank(i, j), end=' ')
        print()

#show_ranks()
#show_maze()