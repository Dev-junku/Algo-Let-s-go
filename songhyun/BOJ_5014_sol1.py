import sys
sys.stdin = open('input.txt')

def bfs(F, S, G, U, D):
    queue = [S]
    visited[S] = 0
    temp = 0
    while queue:
        cur = queue.pop(0)
        if cur < G:
            temp = cur + U
            if visited[temp] == 0:
                visited[temp] = visited[cur] + 1
                queue.append(temp)
        elif cur > G:
            temp = cur - D
            if temp <= 0:
                return 'use the stairs'
            if visited[temp] == 0:
                visited[temp] = visited[cur] + 1
                queue.append(temp)
        else:                                           #찾았으면
            return visited[cur]
    return 'use the stairs'



F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1+U)]

print(bfs(F, S, G, U, D))
# print(visited)

