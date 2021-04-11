from sys import stdin


def bfs():
    if N == K:
        return (0, 1)
    else:
        tovisit = [N]
        visited[N][1] = 1
        count = 1           # 현재 소요 시간

        while not visited[K][1]:    # K 도착시까지
            temp = []
            for _ in range(len(tovisit)):
                v = tovisit.pop()
                for w in (v-1, v+1, v*2):
                    if 0 <= w <= 100000:
                        # 미방문시 다음 방문 계획 추가
                        if not visited[w][0]:
                            temp.append(w)
                            visited[w][0] = count
                        # 이번 시간이 최초 방문 시간이라면, 경우의 수 가산
                        if count <= visited[w][0]:
                            visited[w][1] += visited[v][1]

            tovisit = temp  # 다음 방문
            count += 1

        return(visited[K])


N, K = map(int, stdin.readline().split())
visited = [[0, 0] for _ in range(100001)] # 최초 방문 시점, 해당 지점 도착 횟수

result = bfs()
for i in range(2):
    print(result[i])