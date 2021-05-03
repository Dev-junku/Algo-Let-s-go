# n, s, a, b = 6, 4, 6, 2
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
#

#
def solution(n, s, a, b, fares):
    # 플로이드 와샬, 모든 정점으로부터의 최소 거리 구하고
    # ( 시작점 + x ) + ( x ~ A의 끝점) + (x ~ B의 끝점)
    INF = 10987654321
    answer = INF

    # 초기화
    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0
    # 대각행렬 그래프에 시작과 끝 노드 기준으로 거리값 대입해주기
    for (st, ed, w) in fares:
        dist[st][ed] = w
        dist[ed][st] = w
    # print(dist)

    # 플로이드 와샬 - k: 경유지, i: 출발지, j: 목적지
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 만약 경유지를 거쳐 (2개 거리를 계산)가는 값이 바로 가는 값보다 작다면 두 값을 교체한다
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # print(dist)
    # i로 모든 거리와 비교해보면서 그중 가장 작은 값을 정답으로 출력)
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer

print(solution(n, s, a, b, fares))
