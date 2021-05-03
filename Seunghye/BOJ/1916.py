import heapq

N = int(input())    # 도시 개수
M = int(input())    # 버스 대수

# 간선 연결
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

# 출발점, 도착점
start, end = map(int, input().split())

# 거리 기본 설정
INF = float('inf')
dist = [INF for _ in range(N+1)]

# heap에 push
heap = []
heapq.heappush(heap, (0, start))
dist[start] = 0

# heap에 남은 정점이 있는 동안
while heap:
    cost, v = heapq.heappop(heap)   # 비용, 출발 도시
    if cost > dist[v]:              # 이미 갱신한 도시라면 skip
        continue
    for w, w_cost in graph[v]:      # 인접 도시를 대상으로 갱신 후 heap에 push
        if cost + w_cost < dist[w]:
            dist[w] = cost + w_cost
            heapq.heappush(heap, (dist[w], w))

# 최소비용
print(dist[end])
