import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]                #상우하좌

def dfs1(matrix, row, col):                         #다 같은거
    visited[row][col] = True
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]                             #네방향으로
        if nr < 0 or nr >= T or nc < 0 or nc >= T:
            continue
        if visited[nr][nc] == False:
            if matrix[nr][nc] == matrix[row][col]:
                dfs1(matrix, nr, nc)

def dfs2(matrix, row, col):                         #다 같은거
    visited[row][col] = True
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]                             #네방향으로
        if nr < 0 or nr >= T or nc < 0 or nc >= T:
            continue
        if visited[nr][nc] == False:
            if matrix[nr][nc] == 'G' or matrix[nr][nc] == 'B':
                dfs2(matrix, nr, nc)

T = int(input())
matrix = [0]*T       #일반
matrix2 = []
count1 = 0
count2 = 0
visited = [[False for _ in range(T)]for _ in range(T)]
for i in range(T):
    matrix[i] = list(map(str, input()))
for i in range(T):
    matrix2 += [matrix[i]]
for row in range(T):
    for col in range(T):
        if visited[row][col] == False:
            dfs1(matrix, row, col)
            count1 += 1

visited = [[False for _ in range(T)]for _ in range(T)]
for row in range(T):
    for col in range(T):
        if visited[row][col] == False:
            if matrix[row][col] == 'G' or matrix[row][col] == 'B':
                dfs2(matrix, row, col)
                count2 += 1
            else:
                dfs1(matrix, row, col)
                count2 += 1

print(count1, count2)



