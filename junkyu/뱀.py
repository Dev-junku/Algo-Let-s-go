from collections import deque

# 보드 크기, 사과 개수 받기
N = int(input())
K = int(input())

# 보드 세팅
# 뱀이 있으면 1로 세팅
arr = [[0 for _ in range(N)] for _ in range(N)]
arr[0][0] = 1

# 사과 위치 정보 받기
# 사과는 -1로 세팅!
apple_loc = []
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = -1 # 하.. 여기서 엄청 헤맴..
                       # 왜 -1을 못봤지 ㅜㅜ

# 회전 수 받기
L = int(input())

# 회전 정보 받기
cycle_info = deque()
for _ in range(L):
    x, c = map(str, input().split())
    cycle_info.append((x, c))

# 방향 바꾸기!
def change_direct(direct, dx, dy):

    if direct == 'D':
        if dx == 0 and dy == 1:
            dx, dy = 1, 0
        elif dx == 1 and dy == 0:
            dx, dy = 0, -1
        elif dx == -1 and dy == 0:
            dx, dy = 0, 1
        elif dx == 0 and dy == -1:
            dx, dy = -1, 0

    elif direct == 'L':
        if dx == 0 and dy == 1:
            dx, dy = -1, 0
        elif dx == 1 and dy == 0:
            dx, dy = 0, 1
        elif dx == -1 and dy == 0:
            dx, dy = 0, -1
        elif dx == 0 and dy == -1:
            dx, dy = 1, 0

    return dx, dy


# 이동!
def moving_snake(x, y, cycle_info):
    global arr

    # 초기 데이터 셋팅!
    length = deque()
    length.append((x, y))
    t = 0
    dx = 0
    dy = 1

    # 이건 방향 설정 해주기 위해서 사용할 것임!
    timing, direct = cycle_info.popleft()
    timing = int(timing)

    while True:

        if timing == t:

            dx, dy = change_direct(direct, dx, dy)

            if cycle_info:
                timing, direct = cycle_info.popleft()
                timing = int(timing)

        nx, ny = x + dx, y + dy
        t += 1

        # 만약에 아래 조건에 부합되지 않으면?
        # 즉 N 범위에 벗어났으면서 자기 자신에 부딪힌다면
        # break!
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1:
            x, y = nx, ny

            # 사과가 아닐경우 꼬리와 머리만 이동하면 됨.
            if arr[x][y] != -1:
                px, py = length.popleft()
                arr[px][py] = 0
                length.append((x, y))
                arr[x][y] = 1
            
            # 사과인 경우 몸의 길이가 길어지니까. 머리만 조정!
            elif arr[x][y] == -1:
                length.append((x, y))
                arr[x][y] = 1
        else:
            break
    
    return t

print(moving_snake(0, 0, cycle_info))