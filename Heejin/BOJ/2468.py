
dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

def bfs(col, row):
    queue = [(col, row)]
    while queue:
        c_col, c_row = queue.pop(0)

        for i in range(4):
            n_col = c_col + dcol[i]
            n_row = c_row + drow[i]
            if 0 <= n_row < N and 0 <= n_col < N and visited[n_col][n_row] == 1:
                queue.append((n_col, n_row))
                visited[n_col][n_row] = 0


N = int(input())
area = [list(map(int, input().split(' '))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
m = min([min(L) for L in area])
M = max([max(L) for L in area])

max_area_count = 1
for limit in range(m, M + 1):
    area_count = 0
    # limit보다 작은애들은 0, 큰애들은 1로 놓음. 1이 방문해야하는 애.
    for col in range(N):
        for row in range(N):
            if area[col][row] < limit:
                visited[col][row] = 0
            else:
                visited[col][row] = 1


    # 지역을 돌면서
    for col in range(N):
        for row in range(N):
            # 1이라면
            if visited[col][row] == 1:
                bfs(col, row)
                area_count += 1

    max_area_count = max(max_area_count, area_count)

print(max_area_count)