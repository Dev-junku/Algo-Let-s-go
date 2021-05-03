import sys

res = sys.maxsize
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
half = N // 2

def score(visited):
    global S
    start_score = link_score = 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start_score += S[i][j]
            elif not visited[i] and not visited[j]:
                link_score += S[i][j]

    return abs(start_score - link_score)

def tracking(idx, selected):
    global res, visited

    if selected == half:
        res = min(res, score(visited))
        return

    for i in range(idx, N):
        if visited[idx] == 0:  
            visited[i] = 1
            tracking(i+1, selected+1)
            visited[i] = 0

tracking(0, 0)
print(res)