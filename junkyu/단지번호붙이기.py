from collections import deque

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    global arr, area
    q = deque([(x, y)])
    arr[x][y] = cnt
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = cnt
                area += 1

cnt = 2
nums = []
for i in range(N):
    for j in range(N):
        area = 1
        if arr[i][j] == 1:
            bfs(i, j)
            cnt += 1
            nums.append(area)
            
print(len(nums))
nums.sort()

for num in nums:
    print(num)