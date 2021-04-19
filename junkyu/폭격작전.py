import sys

sys.stdin = open('문제1_input.txt')

# bfs로 순환을 돌 것임.
def bfs(x, y, rang, dx, dy):
    global N_arr, stack
    stack.append(N_arr[x][y])
    N_arr[x][y] = 0
    q = [(x, y)]
    cnt = 0
    # q가 없어도 순회는 중지, cnt가 폭발 범위보다 같아져도 순회 중지
    while cnt < rang and q:
        x, y = q.pop(0)
        # 한쪽 방향으로만 순회
        nx, ny = x + dx, y + dy
        # 새로운 x, y가 범위 내에 있다면
        if 0 <= nx < N and 0 <= ny < N:
            if N_arr[nx][ny] != 0: # 그리고 그 원소값이 0이 아니라면
                # q에 추가
                q.append((nx, ny))
                # stack에는 그 원소 값을 추가
                stack.append(N_arr[nx][ny])
                # 추가 후 해당 원소를 0으로 만듬(중복을 피하기 위함)
                N_arr[nx][ny] = 0
            else: # 만약에 그렇지 않다면(그 원소값이 0이 라면)
                # 일단 q에 추가
                q.append((nx, ny))
                # 스택에도 추가, 0만 추가 될 것이라 연산에 문제 없음
                stack.append(N_arr[nx][ny])
        # 폭발 범위가 증가할 때마다 cnt를 증가
        cnt += 1


# 델타 이동, 중요한 건 한 쪽 방향으로만 갈 수 있음.
Mdx = [1, 1, -1, -1]
Mdy = [1, -1, 1, -1]

T = int(input())

for t in range(1, T+1):
    # 데이터 받기
    N, M = map(int, input().split())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    M_arr = [list(map(int, input().split())) for _ in range(M)]

    # 여기에는 대각선 방향으로만 간 N_arr의 원소를 집어넣어 줄 것임.
    stack = []

    for val in M_arr: # M_arr에 저장한 걸 하나씩 꺼내서
        x, y, rang = val # 함수의 인자로 만들고
        for dx, dy in zip(Mdx, Mdy): # 델타이동을 zip으로 만들어서
            # print(x, y, rang, dx, dy)
            bfs(x, y, rang, dx, dy) # bfs 함수에 집어넣어줌

    print('#{} {}'.format(t, sum(stack)))

