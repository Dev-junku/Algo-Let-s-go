import sys
sys.stdin = open('input.txt')

N = int(input())

tree = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
# BFS
queue = [1]
parent_list = [0] * (N+1)
visited = [False for _ in range(N+1)]

while queue:
    parent = queue.pop(0)
    for i in tree[parent]:
        if not visited[i]:
            parent_list[i] = parent
            queue.append(i)
            visited[i] = True

for i in range(2, N+1):
    print(parent_list[i])
