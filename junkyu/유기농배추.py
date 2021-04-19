from collections import deque

T =  int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def safe(y, x):
    global arr
    if 0 <= y < N and 0 <= x < M:
        if arr[y][x]:
            return True
    return False


def bfs(y, x):
    global arr, visited, dx, dy, cnt
    
    if visited[y][x] == 1:
        return
    
    queue = deque()
    queue.append((y, x))
    cnt += 1
    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not safe(ny, nx):
                continue
            if visited[ny][nx]:
                continue
            else:
                visited[ny][nx] = 1
                queue.append((ny, nx))
    return    
    

for t in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:

                bfs(i, j)
    
    print(cnt)
            

    
    



    