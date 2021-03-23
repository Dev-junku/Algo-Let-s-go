import sys
sys.stdin = open('test.txt')
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            dfs(i)


N, M = map(int,sys.stdin.readline().split(' '))
adj = [[] for i in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
