T = int(input())

# 대각선 방향 델타 이동
delta = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

for tc in range(1, T+1):
    # N 은 적군 지도의 크기, M 은 폭탄의 개수
    N, M = map(int, input().split())
    # enemy 는 적군 지도를 나타낸 2차원 리스트
    enemy = [list(map(int, input().split())) for _ in range(N)]
    # bombs 는 폭탄들의 정보를 담은 2차원 리스트
    bombs = [list(map(int, input().split())) for _ in range(M)]

    # visited 는 방문 정보를 담은, enemy 와 동일한 크기의 2차원 리스트
    # 초기엔 모두 False
    visited = [[False] * N for _ in range(N)]
    # 피해를 입은 적군의 총 수를 담을 변수 cnt 선언
    cnt = 0

    # 폭탄들마다 반복 시행
    for bomb in bombs:
        # 0 부터 폭탄의 화력까지 진행해야 하므로 iterable 을 range(bomb[2]+1)로 잡는다.
        for i in range(bomb[2]+1):
            y = bomb[0]
            x = bomb[1]
            # 대각선 방향 델타 순회
            for dx, dy in delta:
                # 인덱스를 벗어나지 않기 위한 조건과
                # 이미 방문한 곳을 제외하는 조건
                if 0 <= y + dy*i < N and 0 <= x + dx*i < N and not visited[y+dy*i][x+dx*i]:
                    # 방문했으니 True 로 바꾼다.
                    visited[y+dy*i][x+dx*i] = True
                    # 방문한 곳의 적군의 숫자를 cnt 에 더해준다.
                    cnt += enemy[y+dy*i][x+dx*i]
    # 결과 출력
    print('#{} {}'.format(tc, cnt))
