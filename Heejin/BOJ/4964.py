def bfs(col, row):
    queue = [(col, row)]

    while queue:
        for i in range(len(queue)):
            c_col, c_row = queue.pop(0)

            dcol = [-1, 1, 0, 0, 1, -1, 1, -1]
            drow = [0, 0, 1, -1, 1, -1, -1, 1]

            # 팔방탐색
            for i in range(8):
                n_col = c_col + dcol[i]
                n_row = c_row + drow[i]

                if 0 <= n_col < h and 0 <= n_row < w and map_[n_col][n_row]:
                    queue.append((n_col, n_row))
                    map_[n_col][n_row] = 0

while True:
    count = 0
    w, h = map(int,input().split(' '))
    if w == 0 and h == 0:
        break
    map_ = [list(map(int, input().split(' '))) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if map_[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
