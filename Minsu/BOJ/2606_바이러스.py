# 컴퓨터(노드)의 개수 입력
nodes = int(input())
# 네트워크(간선)의 개수 입력
edges = int(input())
# 각각의 네트워크들 입력
lines = [list(map(int, input().split())) for _ in range(edges)]

# 연결 그래프 그리기
graph = [[] for _ in range(nodes + 1)]

for line in lines:
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

# 그래프 모양
# print(graph)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

# 방문 기록
visited = [0 for _ in range(nodes + 1)]

# 스택
stack = [1]

# 자취 남기기
trace = []

# bfs
while stack:
    current = stack.pop()
    if not visited[current]:
        # 방문 표시하기
        visited[current] = 1
        # print('visited',visited)

        # 현재 노드에서 갈 수 있는 곳 스택에 추가하기
        stack += graph[current]
        # print('stack', stack)

        # 자취 기록하기
        trace.append(current)
        # print('trace', trace)

# 1번 컴퓨터를 제외한 나머지 컴퓨터 개수를 출력
print(len(trace) - 1)