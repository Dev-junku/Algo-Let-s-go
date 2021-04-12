# 시간 부족으로 인해 완성하지 못했습니다..
T = int(input())

# 상하좌우 방향 델타 이동
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for tc in range(1, T+1):
    N = int(input())
    stage = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    walls = []
    # 로봇, red zone, green zone, blue zone, 벽의 위치를 저장
    for y in range(len(stage)):
        for x in range(len(stage[y])):
            if stage[y][x] == 2:
                robot = [x, y]
            elif stage[y][x] == 3:
                red = (x, y)
            elif stage[y][x] == 4:
                green = (x, y)
            elif stage[y][x] == 5:
                blue = (x, y)
            elif stage[y][x] == 1:
                walls.append((x, y))
    # zone 의 좌표들이 순서대로 담긴 리스트
    zones = [red, green, blue]
    # 방문한 zone 을 재방문하지 않기 위한 visited 이차원 리스트
    visited_zones = [[False]*N for _ in range(N)]
    # 완료시 탈출 조건
    finished = False
    while not finished:
        x, y = robot[0], robot[1]
        tmp = 0
        # 상하좌우 델타 순회
        for dx, dy in delta:
            # 인덱스를 벗어나지 않고, 방문한 zone 이 아니고, 벽이 아니라면
            if 0 <= x + dx < N and 0 <= y + dy < N and not visited_zones[y+dy][x+dx] and (x + dx, y + dy) not in walls:
                tmp += 1
                # 방문한 곳이 zone 이라면 visited 에 True 로 바꾼다.
                if (x + dx, y + dy) in zones:
                    visited_zones[y+dy][x+dx] = True
                    # 현재까지 간 거리를 저장
                    cnt += tmp
                # robot 의 현재 위치
                robot = [x + dx, y + dy]
        # 다 방문했다면 finished = True
        # 방문 불가능한 zone 고려하는 것을 생각하지 못했습니다..
        visited_count = 0
        for x, y in zones:
            if visited_zones[y][x]:
                visited_count += 1
            if visited_count == 3:
                finished = True

    print('#{} {}'.format(tc, cnt))
