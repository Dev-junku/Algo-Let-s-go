# n개의 벽장, 2개의 열린 벽장
# 벽장문은 열린 벽장으로 밀어서 옮길 수 있음
# 특정 벽장을 열기 위해서는 벽장문을 좌/우 한 쪽으로 밀어서 열어야
# -> 해당 방향에서 가장 가까운 열린 벽장을 닫게 됨 -> 거리 = 벽장 추가 이동 횟수
# -> 옮긴 후 열린 벽장 조합(a, b)별 최소 이동횟수 저장

def dfs(u, i, j):
    if u > U:
        return

    t = c_use[u]
    # j i t에서 왼쪽으로 밀기 -> i가 닫힘
    if t > i:
        c_open[u][t][j] = min([c_open[u-1][i][j] + t - i, c_open[u][t][j]])
        dfs(u+1, t, j)
    # t j i에서 오른쪽으로 밀기 -> j가 닫힘
    elif t < j:
        c_open[u][i][t] = min([c_open[u-1][i][j] + j - t, c_open[u][i][t]])
        dfs(u+1, i, t)
    else:
        # j t i에서 왼쪽으로 밀기 -> j가 닫힘
        c_open[u][i][t] = min([c_open[u-1][i][j] + t - j, c_open[u][i][t]])
        dfs(u+1, i, t)
        # j t i에서 오른쪽으로 밀기 -> i가 닫힘
        c_open[u][t][j] = min([c_open[u-1][i][j] + i - t, c_open[u][t][j]])
        dfs(u+1, t, j)

N = int(input())
a, b = map(lambda x: int(x)-1, input().split())            # 최초 열린 벽장
if b > a:
    a, b = b, a

# 사용할 벽장 순서
U = int(input())
c_use = [0] + [int(input())-1 for _ in range(U)]

# 열린 벽장 조합: c_open[u][i][j]는 u번째 순서 기준 i, j번 벽장이 열린 조합까지의 최소 이동거리.
c_open = [[[N*20 for _ in range(N)] for _ in range(N)] for _ in range(U+1)]
c_open[0][a][b] = 0

# 벽장문 이동
dfs(1, a, b)

# 최소값 출력
print(min(min(c_open[U][i]) for i in range(1, N)))