import sys

dat = sys.stdin.readline

N = 9

def row_valid(x, val):
    if val in sudoku[x]:
        return False
    return True


def col_valid(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    
    return True


def square_valid(x, y, val):
    x_mod = x//3
    y_mod = y//3

    for i in range(3):
        for j in range(3):
            if val == sudoku[3*x_mod+i][3*y_mod+j]:
                return False
    return True
    

def tracking(idx):
    global arr

    if idx == num:
        for r in sudoku:
            for n in r:
                print(n, end = ' ')
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            x, y = zero_points[idx][0], zero_points[idx][1]
            if row_valid(x, i) and col_valid(y, i) and square_valid(x, y, i):
                sudoku[x][y] = i
                tracking(idx+1)
                sudoku[x][y] = 0

sudoku = [list(map(int, dat().split())) for _ in range(N)]

zero_points = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_points.append((i, j))

num = len(zero_points)

tracking(0)