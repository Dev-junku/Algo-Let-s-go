from heapq import heappush, heappop

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

cities = [[] for _ in range(N+1)]  # 도시 간 비용을 나타내는 2차원 리스트

# 버스정보: 시작지, 도착지, 요금 입력
for i in range(M):
    s, e, c = map(int, input().split())
    cities[s].append((e, c))

start, end = map(int, input().split())  # 출발점, 도착점

INF = int('inf')

# start에서 특정 도시까지 가는데 걸리는 최소한의 비용
min_cost = [INF for _ in range(N+1)]
min_cost[start] = 0

hq = []  # 힙큐
heappush(hq, (0, start))

while hq:
    cost, current = heappop(hq)

    # 현재 구한 비용이 더 적으면 그냥 넘어가기
    if min_cost[current] < cost:
        continue

    # 현재 노드를 순회하면서 거쳐가기
    for node, node_cost in cities[current]:
        if min_cost[node] > node_cost + cost:  # 최소 비용보다 지금 구한 비용이 더 적으면 교체
            min_cost[node] = node_cost + cost
            heappush(hq, (node_cost, node))  # 그 노드를 거쳐 가는 버스노선들 추가

print(min_cost[end])

