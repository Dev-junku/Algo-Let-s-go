from sys import stdin

# 모든 종류의 테트로미노
tetromino = [
    # 정사각형
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # 직사각형
    [(0, i) for i in range(4)], [(i, 0) for i in range(4)],
    # L, T
    *[[(0, i) for i in range(3)] + [(1, j)] for j in range(3)],
    *[[(1, i) for i in range(3)] + [(0, j)] for j in range(3)],
    *[[(i, 0) for i in range(3)] + [(j, 1)] for j in range(3)],
    *[[(i, 1) for i in range(3)] + [(j, 0)] for j in range(3)],
    # S
    [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(1, 0), (1, 1), (0, 1), (0, 2)], [(0, 0), (0, 1), (1, 1), (1, 2)],
]

N, M = map(int, stdin.readline().split())                               # 세로 크기 N, 가로 크기 M
paper = [list(map(int, stdin.readline().split())) for _ in range(N)]    # 종이에 쓰여있는 수

result = 0                                                              # 최대 누적합
# 모든 원소를 출발점으로
for i in range(N):
    for j in range(M):
        # 모든 종류의 테트로미노 시도
        for tet in tetromino:
            total = 0   # 내부 누적합
            for r, c in tet:
                # 범위 이탈 시 종료
                if 0 <= i + r < N and 0 <= j + c < M:
                    total += paper[i+r][j+c]
                else:
                    break
            else:
                # 범위 이탈 없이 누적합을 초과하면 갱신
                if total > result:
                    result = total

print(result)
