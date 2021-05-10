import heapq

def solution(n, s, a, b, fares):
    # 정점: 1~n. 3 <= n <= 200                    1 <= s, a, b <= n, s != a != b
    # fares: c지점, d지점, 요금 f. 무방향 그래프.     1 <= f <= 100000
    
    # 최저 택시요금 합 구하기
    # s에서 각 정점까지의 거리
    # 각 정점에서 a, b까지의 거리 = a, b에서 각 정점까지의 거리
    # s와 위 둘의 합 -> 최저치가 결과

    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    INF = float('inf')
    dist = [[INF for _ in range(n+1)] for _ in range(3)]  # s에서의 거리, a에서의 거리, b에서의 거리 저장
    start = [s, a, b]                                     # 출발 정점
    
    for nth in range(3):
        # 다익스트라
        # 시작 정점에서 시작
        start_node = start[nth]
        dist[nth][start_node] = 0                       # 출발지에서는 소요시간이 없음
        q = []
        heapq.heappush(q, (0, start_node))
        
        while q:
            # 가장 가까운 정점을 찾음
            d, v = heapq.heappop(q)
            
            # 그 주변의 인접 정점 갱신
            for w, f in graph[v]:
                new_dist = dist[nth][v] + f
                if new_dist < dist[nth][w]:
                    dist[nth][w] = new_dist
                    heapq.heappush(q, (new_dist, w))
    
    answer = min(map(lambda x: dist[0][x]+dist[1][x]+dist[2][x], range(1, n+1)))
    return answer