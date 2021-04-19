from sys import stdin


def bfs():
    if N == K:
        return 0

    visited = [0 for _ in range(100001)]
    tovisit = [N]

    count = 1
    while tovisit:
        temp = []
        for _ in range(len(tovisit)):
            v = tovisit.pop()
            for w in (v + 1, v - 1, v * 2):
                if w == K:
                    return count    # 찾았으면 종료
                if -1 < w < 100001 and not visited[w]:
                    temp.append(w)
                    visited[w] = count
        tovisit = temp
        count += 1


N, K = map(int, stdin.readline().split())
print(bfs())
