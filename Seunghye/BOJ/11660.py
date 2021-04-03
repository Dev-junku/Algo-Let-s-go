from sys import stdin

N, M = map(int, stdin.readline().split())

# 테이블 생성: 0행, 0열을 포함
table = [[0 for _ in range(N+1)]]
table.extend([0, *map(int, stdin.readline().split())] for _ in range(N))

# 0, 0에서 해당 지점까지의 누적합
for i in range(1, N+1):
    for j in range(1, N+1):
        table[i][j] += (table[i-1][j] + table[i][j-1] - table[i-1][j-1])

# 구간합: 0, 0부터 x2, y2까지의 합 - 위쪽 제거(0행부터 x1-1 행까지) - 왼쪽 제거(0열부터 y1-1열까지) + 중복 제거된 구간 복구(0, 0부터 x1-1, y1-1까지)
for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1])
