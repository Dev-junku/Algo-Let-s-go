def solution(a, edges):
    if sum(a):
        return -1
    else:
        # 연결된 노드를 나타내는 리스트
        Vertex = [[] for _ in range(len(a))]
        visited = [0] * (len(a))
        for idx in range(len(edges)):
            Vertex[edges[idx][0]].append(edges[idx][1])
            Vertex[edges[idx][1]].append(edges[idx][0])

        stack = []

        # 총 횟수
        turn = 0

        # 맨 끝에 있는 노드부터 처리,
        for idx in range(len(Vertex)):
            if len(Vertex[idx]) == 1:
                # 턴을 추가하고
                turn += abs(a[idx])
                # 인접한 노드의 가중치를 상쇄시키고
                a[Vertex[idx][0]] += a[idx]
                a[idx] = 0
                # 그 노드를 스택에 추가
                if Vertex[idx][0] not in stack:
                    stack.append(Vertex[idx][0])
                # 방문표시
                visited[idx] = 1

        while stack:
            for aa in a:
                if aa != 0:
                    break
            else:
                return turn
            current = stack.pop(0)
            turn += abs(a[current])
            visited[current] = 1

            print(Vertex)
            print(a)
            print(current)
            print(visited)
            for node in Vertex[current]:
                if visited[node] == False:
                    a[node] += a[current]
                    a[current] = 0
                    stack.append(node)



    return turn






print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))