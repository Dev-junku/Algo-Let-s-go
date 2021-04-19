from pandas import DataFrame
from collections import deque

T = int(input()) # 테스트 케이스 갯수

# 델타 이동
dx = [2, 2, 1, 1, -1, -1, -2, -2] 
dy = [1, -1, 2, -2, -2, 2, -1, 1]


def bfs(sx, sy, ex, ey):
    global arr
    queue = deque()
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            return arr[ex][ey]-1
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

for t in range(1, T+1):
    I = int(input())
    arr = [[0 for _ in range(I)] for _ in range(I)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    arr[sx][sy] = 1 # 시작점
    print(bfs(sx, sy, ex, ey))




    
