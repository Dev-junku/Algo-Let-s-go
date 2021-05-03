from collections import deque


def get_direction(current_direct, d):
    if d == 'D':
        current_direct += 1
        if current_direct > 3:
            current_direct -= 4
    else:
        current_direct -= 1
        if current_direct < 0:
            current_direct += 4
    return current_direct

# input 받기
D = [
    (0, -1), # 왼쪽
    (-1, 0), # 위
    (0, 1), # 오른쪽
    (1, 0), # 아래
]
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

board = [[0] * N for _ in range(N)]
snake = deque()

for _ in range(K):
    a, b = list(map(int, input().split()))
    board[a-1][b-1] = 1

L = int(input())
times = {}
for i in range(L):
    x, c = input().split()
    times[int(x)] = c


current_direct = 2 # 오른쪽 보고있음.
sec = 1
snake.append((0, 0))
while True:
    # 정해진 방향으로 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    head = snake[0]
    cur_head = (head[0] + D[current_direct][0], head[1] + D[current_direct][1])

    # 현재 머리가 있는 곳이 뱀의 몸 어느곳이이거나 벽이 아니면 진행.
    if cur_head not in snake and 0 <= cur_head[0] < N and 0 <= cur_head[1] < N:
        snake.appendleft(cur_head)

        # 뱀이 이동한 머리에 사과가 있다면?
        if board[cur_head[0]][cur_head[1]] == 1:
            # 사과 있는자리 0 으로 만들어줘.
            board[cur_head[0]][cur_head[1]] = 0
        # 뱀이 이동한 머리에 사과가 없다면 꼬리가 위치한 칸을 비워준다.
        else:
            snake.pop()
        # 시간 체크하기.
        if sec in times.keys():
            current_direct = get_direction(current_direct, times[sec])
        sec += 1
    # 본인 몸이나, 벽에 부딪힌 경우
    else:
        break

print(sec)




