from collections import deque

dx = [0, 1, 0, -1, -1, 1, -1, 1]
dy = [1, 0, -1, 0, -1, 1, 1, -1]


def bfs(x, y):
    global arr, cnt
    arr[x][y] = 2
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 2
                    q.append((nx, ny))
    cnt += 1
    
while True:
    try:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
    except:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
    
    print(cnt)
