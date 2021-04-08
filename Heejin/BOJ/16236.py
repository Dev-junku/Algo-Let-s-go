import sys
sys.stdin = open("input.txt")

dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]
target_spot = []
def bfs(col, row):
    global baby, fish_food, distance
    # 현재 아기 상어 자리.
    queue = [(col, row)]
    while queue:
        # 단계를 알 수 있게 하는 for문.
        for _ in range(len(queue)):
            distance += 1 # 한 단계 지날 때 마다 상어로부터 거리 하나씩 늘어가.
            ccol, crow = queue.pop()
            for i in range(4):
                ncol = ccol + dcol[i]
                nrow = crow + drow[i]

                if 0 <= ncol < length and 0 <= nrow < length:
                    # 만약에 범위 안에 들고, 아기 상어보다 작다면, 갈 수 있는 지점임.
                    if 0 < matrix[ncol][nrow] < baby:
                        target_spot.append((ncol, nrow))

            # 포문이 끝나고 target_spot에 뭐라도 있으면 하나씩 살펴봄.
            if len(target_spot) > 0:
                # target_spot을 맨위, 맨 왼쪽이 기준이므로 맨위로 먼저 정렬, 그다음 맨 왼쪽으로 정렬함.
                target_spot.sort(key=lambda x: (x[0], x[1]))
                # 정렬된 맨 앞이 이동할 곳
                first_target_spot = target_spot.pop(0)
                # 물고기 먹은 자리에 0
                matrix[first_target_spot[0]][first_target_spot[1]] = 0
                # 상어가 고기 한마리 먹음.
                fish_food += 1
                # 상어가 고기 자기크기 만큼 먹으면 1 커짐
                if fish_food == baby:
                    baby += 1
                    fish_food = 0
                # 현재 상어자리 초기화 0
                matrix[ccol][crow] = 0
                # 상어가 그 자리로 이동
                queue.append(first_target_spot)

length = int(input())
matrix = [list(map(int, input().split())) for _ in range(length)]

# 아기상어의 위치 찾기
baby = 9
fish_food = 0
distance = 0
for col in range(length):
    for row in range(length):
        if matrix[col][row] == baby:
            bfs(col, row)
# 1. 먹을 수 있는 물고기 1개면 그거 먹으러감
# 2. 먹을수 있는게 많으면 가장 가까운애.
# 3. 거리 가까운애 많으면 젤 위, 여러마리면 젤 왼쪽.

# 상어가 다 먹었을 때 어떻게 체크하지?