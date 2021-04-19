from collections import deque

N, M, V = map(int, input().split())

mat = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    mat[v1][v2] = 1
    mat[v2][v1] = 1

def bfs(start):
    visited = [start]
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in range(len(mat)):
            if mat[v][i] == 1 and (i not in visited):
                visited.append(i)
                q.append(i)
    return visited


def dfs(start, visited):
    visited += [start]
    for i in range(len(mat)):
        if mat[start][i] == 1 and (i not in visited):
            dfs(i, visited)
    return visited

print(*dfs(V, []))
print(*bfs(V))



