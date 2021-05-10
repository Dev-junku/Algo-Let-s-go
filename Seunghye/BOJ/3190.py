from collections import deque

# 보드판 생성
N = int(input())
board = [[-1 for _ in range(N+2)]] + [[-1, *[0 for _ in range(N)], -1] for _ in range(N)] + [[-1 for _ in range(N+2)]]

# 사과 배치
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    board[i][j] = 1

# 이동 방향: 우, 하, 좌, 상
dis = [0, 1, 0, -1]
djs = [1, 0, -1, 0]
L = int(input())
turns = deque()         # 회전 시점
for _ in range(L):
    time, way = input().split()
    turns.append((int(time), 1 if way == 'D' else -1))  # 우측 회전 시 +1, 좌측 회전 시 -1

snake = deque()         # 뱀의 전체 영역
snake.append((1, 1))
count = 0               # 경과한 시간
d = 0                   # 현재 이동 방향

while True:
    count += 1          # 시간 경과

    # 머리 이동
    i, j = snake[-1]
    i += dis[d]
    j += djs[d]

    # 벽이나 자기 자신과 부딪히면 종료
    if board[i][j] < 0 or (i, j) in snake:
        break
    # 벽이 아니라면, 머리 이동
    else:
        snake.append((i, j))
        # 사과가 없다면 꼬리칸 비우기
        if not board[i][j]:
            snake.popleft()
        # 사과 없애기
        board[i][j] = 0

    # 회전 시점이 오면 방향 전환
    if turns and count == turns[0][0]:
        _, way = turns.popleft()
        d += way
        if d < 0:
            d += 4
        elif d > 3:
            d -= 4

print(count)
