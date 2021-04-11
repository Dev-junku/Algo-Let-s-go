import sys
sys.stdin = open('input.txt')

move = [[-1, 0], [0, 1], [1, 0], [0, -1]] #상우하좌

def bfs():
    queue = []



T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [0]*N
    for idx in range(N):
        matrix[idx] = list(map(int, input.split()))
    visited = [[False for _ in range(N)] for _ in range(N)]
    baby_shark = 2
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 9:
                bfs(row,col)


#접근법