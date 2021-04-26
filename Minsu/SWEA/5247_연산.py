import sys
sys.stdin = open('sample_input.txt')


def solution():

    queue = [0] * 1000001  # (숫자)
    queue[0] = N

    visited = [0] * 1000001  # (방문 여부, 횟수)

    # pop(0) 역할의 인덱스
    front = -1
    # push 역할의 인덱스
    rear = 0

    while front != rear:

        front += 1

        current = queue[front]

        next_nums = [current-1, current+1, current*2, current-10]

        # 조건에 부합하면 queue에 넣어주기
        for num in next_nums:

            if 1 <= num <= 1000000 and visited[num] == 0:
                rear += 1
                queue[rear] = num
                visited[num] = visited[current] + 1 # 숫자별로 거리 기록하기

            # 종료 조건
            if num == M:
                return visited[num]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, solution()))

