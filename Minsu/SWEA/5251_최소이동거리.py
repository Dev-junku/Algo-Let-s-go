import sys
sys.stdin = open('sample_input.txt')

def dijkstra():
    INF = float('inf')
    # 0번 노드에서 다른 노드까지의 최소 거리 리스트
    dist = [INF for _ in range(N+1)]
    dist[0] = 0
    # 방문 여부
    visited = [False for _ in range(N+1)]

    for _ in range(N+1):
        min_dist = INF
        for i in range(N+1):
            # 방문하지 않았고, 최소거리인 노드를 찾아서
            if not visited[i] and min_dist > dist[i]:
                min_dist = dist[i]
                idx = i  # 인덱스도 저장

        visited[idx] = True  # 방문 표시

        for j in range(N+1):
            # 노드에 갈 수 있고, 현재 비용보다 노드를 거쳐 거리보다 가깝다면
            if matrix[idx][j] and dist[idx] + matrix[idx][j] < dist[j]:
                dist[j] = dist[idx] + matrix[idx][j]

    return dist[N]


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())  # 연결지점 번호 N, 도로의 개수 E

    # 노드 간의 거리를 나타내는 2차원 리스트
    matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

    # 노드 간 거리 입력
    for road in range(E):
        s, e, w = map(int, input().split())  # 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w
        matrix[s][e] = w

    print('#{} {}'.format(tc, dijkstra()))
