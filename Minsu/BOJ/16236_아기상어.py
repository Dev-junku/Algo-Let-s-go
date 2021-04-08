# 먹을 수 있는 물고기 찾는 함수
def search_fish():
    edible_fish = []
    for i in range(N):
        for j in range(N):
            if 0 < space[i][j] < size:
                edible_fish.append((j, i))
    return edible_fish


# bfs(먹을 수 있는 물고기 까지의 거리를 구하는 함수)
def bfs(space, loc_x, loc_y):
    visited = [[0] * N for _ in range(N)]
    queue = [(loc_x, loc_y)]
    count = 0

    # 델타 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        loc_x, loc_y = queue.pop(0)
        for i in range(4):
            nloc_x = loc_x + dx[i]
            nloc_y = loc_y + dy[i]
            count += 1

            # 탐색에 필요한 조건들
            # 범위 안
            if 0 <= nloc_x < N and 0 <= nloc_y < N:
                # 방문하지 않은 곳
                if visited[nloc_y][nloc_x] == 0:
                    if space[nloc_y][nloc_x] <= size:
                        queue.append((nloc_x, loc_y))
                        visited[nloc_y][nloc_x] = 1





N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

# 처음 크기
size = 2

# 처음 위치
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            loc_x = j
            loc_y = i
            break

# 먹을 수 있는 물고기
edible_fish = search_fish()
print(edible_fish)

# 물고기까지의 거리
bfs(edible_fish, loc_x, loc_y)

