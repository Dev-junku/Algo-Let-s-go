import sys
sys.stdin = open('input.txt')


move = [[-1,0],[0,1],[1,0],[0,-1]] # 상우하좌
def bfs1(matrix, visited, row, col):
    queue = []
    queue += [[row,col]]
    visited[row][col] = True
    while queue:
        cur = queue.pop(0)
        for i in move:
            nr = cur[0] + i[0]
            nc = cur[1] + i[1]
            if nr < 0 or nr >= T or nc < 0 or nc >= T:
                continue
            if matrix[cur[0]][cur[1]] == matrix[nr][nc] and visited[nr][nc] == False:       #같고 방문 없으면 queue에 enqueue
                visited[nr][nc] = True
                queue += [[nr, nc]]


def bfs2(matrix, visited, row, col):
    queue = []
    queue += [[row,col]]
    visited[row][col] = True
    while queue:
        cur = queue.pop(0)
        for i in move:
            nr = cur[0] + i[0]
            nc = cur[1] + i[1]
            if nr < 0 or nr >= T or nc < 0 or nc >= T:
                continue
            if matrix[nr][nc] == 'G' or matrix[nr][nc] == 'R':       #같고 방문 없으면 queue에 enqueue
                if visited[nr][nc] == False:
                    visited[nr][nc] = True
                    queue += [[nr, nc]]


T = int(input())
matrix = [0]*T
count1 = 0
count2 = 0
visited = [[False for _ in range(T)]for _ in range(T)]
for i in range(T):
    matrix[i] = list(map(str, input()))

for row in range(T):
    for col in range(T):
        if visited[row][col] == False:
            bfs1(matrix, visited, row, col)
            count1 += 1

visited = [[False for _ in range(T)]for _ in range(T)]
for row in range(T):
    for col in range(T):
        if visited[row][col] == False:
            if matrix[row][col] == 'R' or matrix[row][col] == 'G':
                bfs2(matrix, visited, row, col)
                count2 += 1
            else:
                bfs1(matrix, visited, row, col)
                count2 += 1

print(count1, count2)