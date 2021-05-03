# import sys
from heapq import heappush, heappop
# sys.stdin = open('input.txt')


# 1-1. heapq로 우선순위 큐 구현
def Dijkstra(K, graph, V):
    heap = []
    # 거리정보
    distance = [1e9] * (V + 1)
    distance[K] = 0
    # 최단거리로 오기 전 경로를 저장
    cource = [0] * (V + 1)
    heappush(heap, (0, K))

    # 우선순위 큐
    while heap:
        weight, location = heappop(heap)

        if distance[location] < weight:
            continue

        for l, w in graph[location]:
            w += weight
            if w < distance[l]:
                distance[l] = w
                cource[l] = location
                heappush(heap, (w, l))
    return cource


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

# 0. 양방향 그래프 만들기
for _ in range(E):
    st, ed, w = map(int, input().split())
    graph[st].append([ed, w])
    graph[ed].append([st, w])

# 1. 인덱스 1부터 V개까지 다익스트라 알고리즘 실행
for idx in range(1, V+1):
    # 1-2. 실행 후 최단거리를 만들어 준 전 경로를 course에 저장
    course = Dijkstra(idx, graph, V)

    ret = ['-'] * (V + 1)

    # 2. 현재 집하장과 탐색 시작점이 같으면 자기 자신이므로 - 출력
    for jdx in range(1, V + 1):
        if idx == jdx:
            continue
        checkIndex = jdx

        # 2-1. 시작 집하장이 나올 때까지 반복한다
        while 1:
            kdx = course[checkIndex]
            # 시작 집하장 나오면 끝
            if kdx == idx:
                ret[jdx] = checkIndex
                break
            # 전 경로로 올라가기
            checkIndex = kdx
    # 3. 결과 한 줄씩 출력
    for i in range(1, V + 1):
        print(ret[i], end=' ')
    print()