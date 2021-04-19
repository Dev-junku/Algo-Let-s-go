from collections import deque

N = int(input())

empty = []
fish = []
shark = []
baby_M = 2
location = []
caneat = [[0]*N for _ in range(N)]

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            empty.append([i,j])
        elif arr[i][j] == 9:
            shark.append([i,j])
        else:
            fish.append([i, j, arr[i][j]])

# 델타
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global arr, baby_M
    queue = []
    queue.append((x, y))
    cnt = 0
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                if arr[nx][ny] > arr[cx][cy]:
                    continue
                if arr[nx][ny] == arr[cx][cy]:
                    queue.append((nx, ny))

                if arr[nx][ny] < arr[cx][cy]:
                    queue.append((nx, ny))
                    arr[nx][ny] = 0
                    cnt += 1
                    if cnt == baby_M:
                        baby_M += 1

# 아기 상어의 위치는 항상 하나여야 한다.

def distance(shark_l, fish_l): # 좌표값만 넣자..
    global arr, baby_M, location, caneat
    for f in fish:
        for s in shark:
            if 0 < arr[f[0]][f[1]] < baby_M:
                caneat[f[0]][f[1]] = 1
                dista = abs(shark_l[0][0]-f[0]) + abs(shark_l[0][1]-f[1])
                location.append([f[0], f[1], dista])
    return 

distance(shark, fish)
print(caneat, location)
if len(location) > 1:
    
# def time(empty, shark, fish):
#     if not fish:
#         return 0