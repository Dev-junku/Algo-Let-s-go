from sys import stdin

def find_root(x):
    if r[x] != x:
        r[x] = find_root(r[x])
    return r[x]

def union(x, y):
    rx, ry = find_root(x), find_root(y)
    r[rx] = ry


N, M = map(int, stdin.readline().split())
r = [i for i in range(N+1)]
# 크루스칼 알고리즘을 위해 가중치에 따라 정렬
roads = sorted([list(map(int, stdin.readline().split())) for _ in range(M)], key=lambda x: x[2])

# 최소 신장 트리만 남긴 후 하나의 도로만 없애면, 서로 연결되어 있는 2개의 마을로 분할됨
N -= 1      # 남은 도로 수
r_idx = 0   # 확인할 도로
costs = 0   # 유지비용
while N:
    a, b, c = roads[r_idx]
    # 사이클이 아니라면 해당 간선 선택
    if find_root(a) != find_root(b):
        union(a, b)
        N -= 1
        # 마지막 도로를 제외하고 유지비용 계산
        if N:
            costs += c
    r_idx += 1

print(costs)
