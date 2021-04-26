def find_set(x):
    if repr_node[x] != x:
        repr_node[x] = find_set(repr_node[x])
    return repr_node[x]

def union(x, y):
    rx, ry = find_set(x), find_set(y)
    repr_node[ry] = rx


N = int(input())
M = int(input())

# 서로소 집합의 대표 원소 저장
repr_node = [i for i in range(N+1)]

# 비용 오름차순 정렬
graphs = [list(map(int, input().split())) for _ in range(M)]
graphs.sort(key=lambda x: x[2])

N -= 1      # 남은 간선 수
i = 0       # 네트워크 선 번호
total = 0   # 누적 비용

while N:
    x, y, w = graphs[i]
    # 연결 시 사이클 발생 여부 확인
    rx, ry = find_set(x), find_set(y)
    if rx != ry:
        # 사이클이 발생하지 않는다면 비용 가산 후 합집합
        total += w
        union(rx, ry)
        N -= 1
    i += 1

print(total)
