import sys
sys.stdin = open('input.txt')

from collections import deque


def solution(cave):
    # start 는 [y좌표, x좌표, 도둑루피의 크기]
    start = [0, 0, cave[0][0]]

    def bfs(start):
        inf = 9999999999
        # matrix 는 누적 잃는 금액을 담을 행렬
        matrix = [[inf]*len(cave) for _ in range(len(cave))]
        # 0,0 위치의 값은 동일하다
        matrix[0][0] = cave[0][0]
        # 델타 이동
        dys = [-1, 1, 0, 0]
        dxs = [0, 0, -1, 1]

        queue = deque()
        queue.append(start)
        while queue:
            y, x, cost = queue.popleft()
            # 델타 이동
            for idx in range(len(dys)):
                dy, dx = dys[idx], dxs[idx]
                if 0 <= y + dy < len(cave) and 0 <= x + dx < len(cave):
                    # 만약 이동하려는 곳의 matrix 에 이미 적혀진 누적금액이
                    # 현재까지의 금액 + 이동하려는 곳의 cost 보다 크다면
                    if matrix[y+dy][x+dx] > cost + cave[y+dy][x+dx]:
                        # 금액을 바꿔준다
                        matrix[y+dy][x+dx] = cost + cave[y+dy][x+dx]
                        queue.append([y+dy, x+dx, cost + cave[y+dy][x+dx]])
        return matrix[-1][-1]
    return bfs(start)


# input 처리
tc = 0
while True:
    N = int(input())
    if not N:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    tc += 1

    print('Problem {}: {}'.format(tc, solution(cave)))
