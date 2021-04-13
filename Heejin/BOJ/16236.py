INF = 1e9

dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

def bfs():
    global baby, fish_food, distance
    dist = [[-1] * length for _ in range(length)]
    # 현재 아기 상어 자리.
    queue = [(now_col, now_row)]
    dist[now_col][now_row] = 0
    while queue:
        cur_col, cur_row = queue.pop(0)
        for i in range(4):
            ncol, nrow = cur_col + dcol[i], cur_row + drow[i]
            if 0 <= ncol < length and 0 <= nrow < length:
                if dist[ncol][nrow] == -1 and matrix[ncol][nrow] <= shark_size:
                    dist[ncol][nrow] = dist[cur_col][cur_row] + 1
                    queue.append((ncol, nrow))
    return dist


def find(dist):
    min_dist = INF
    x = y = 0
    for col in range(length):
        for row in range(length):
            if dist[col][row] != -1 and 1 <= matrix[col][row] < shark_size:
                if dist[col][row] < min_dist:
                    # 작은애 갱신 해주고,
                    min_dist = dist[col][row]
                    x, y = col, row
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


length = int(input())
matrix = [list(map(int, input().split())) for _ in range(length)]

# 아기상어의 위치 찾기
shark_size = 2
now_col, now_row = 0, 0
for col in range(length):
    for row in range(length):
        if matrix[col][row] == 9:
            now_col = col
            now_row = row
            matrix[col][row] = 0
result = 0
ate = 0
while True:
    value = find(bfs())

    if value == None:
        print(result)
        break
    else:
        now_col, now_row = value[0], value[1]
        result += value[2]

        matrix[now_col][now_row] = 0
        ate += 1

        if ate >= shark_size:
            shark_size += 1
            ate = 0