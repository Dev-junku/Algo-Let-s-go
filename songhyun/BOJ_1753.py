import sys
sys.stdin = open('input.txt')

INF = 1000000000
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and visited[i] == False:
            min_value = distance[i]
            index = i
    return index

def djikstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
    #여기서는 최소거리를 찾아오기
        now = get_smallest()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            #now에서 j[1] 즉 다음에 도달하는 노드까지 거리의 합 cost
            #지금까지 디스턴스에서  다음 거리 추가
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                #distance[j[0]]은 다음에 도달하는 거리 보다 cost가 작다면 distance switch
                #distance

djikstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])