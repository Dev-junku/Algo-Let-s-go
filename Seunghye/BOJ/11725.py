from sys import stdin

N = int(stdin.readline())
# 연결 저장
links = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    links[a].append(b)
    links[b].append(a)

# 1번 노드부터 BFS
parents = [0 for _ in range(N+1)]   # 부모 노드 저장
parents[1] = -1                     # 예외 처리
tovisit = [1]
while tovisit:
    v = tovisit.pop(0)
    for w in links[v]:
        if not parents[w]:
            parents[w] = v
            tovisit.append(w)

for i in range(2, N+1):
    print(parents[i])
