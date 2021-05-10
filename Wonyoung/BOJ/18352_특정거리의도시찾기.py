from collections import deque

n, m, k, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = [-1] * (n+1)
# 0. 출발거리의 최단 거리를 0으로
answer[s] = 0

# 1. 단방향으로 연결된 도로 정보를 넣는다.
for _ in range(m):
    st, ed = map(int, input().split())
    graph[st].append(ed)

# 2. bfs로 탐색
q = deque([s])
while q:
    v = q.popleft()
    # 2-1. 아직 방문하지 않은 도시면 1 더한값 저장
    # 큐에 넣고 다음 탐색할 곳 지정
    for i in graph[v]:
        if answer[i] == -1:
            answer[i] = answer[v] + 1
            q.append(i)
# 3. 만약 최단거리가 k라면 그 도시를 출력
for j in range(n+1):
    if answer[j] == k:
        print(j)
# 4. 답이 없으면 -1 출력
if k not in answer:
    print(-1)