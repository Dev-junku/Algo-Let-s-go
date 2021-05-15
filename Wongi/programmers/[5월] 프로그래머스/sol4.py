"""
이 트리의 루트 노드는 1번 노드
1번 쿼리: 정수 u가 주어집니다. u번 노드의 서브 트리의 모든 노드의 값의 합을 구해야 합니다.
2번 쿼리: 정수 u, w가 주어집니다. u번 노드의 값을 삭제한 뒤, u번 노드의 부모 노드의 값을 u번 노드로 복사합니다.
u번 노드의 부모 노드에 대해 같은 작업을 반복하며 루트노드까지 거슬러 올라갑니다. 마지막으로 루트 노드의 값을 w로 바꿉니다.
"""

def solution(values, edges, queries):
    answer = []
    values = values
    V = len(values)
    G = [[] for _ in range(V + 1)]
    parent = [[] for _ in range(V + 1)]
    # parent = [0] * (V + 1)
    for edge in edges:
        v, u = edge
        G[v].append(u)
        parent[u].append(v)
        # parent[u] = v

    def subtree(v):
        visited = [0] * (V + 1)
        visited[v] = 1
        Q = [v]
        total = 0
        while Q:
            cur_v = Q.pop()
            total += values[cur_v - 1]
            for w in G[cur_v]:
                if not visited[w]:
                    visited[w] = 1
                    Q.append(w)
        return total

    def change_parent_node(v, value):
        # 1) 우선은 이진트리라고 가정하고 풀이
        # while parent[v]:
        #     p = parent[v]
        #     values[v - 1] = values[p - 1]
        #     v = p
        # values[0] = value

        # 2) 여러 부모 노드가 존재??
        Q = [v]   # list
        while Q:
            cur_p = Q.pop()
            for p_node in parent[cur_p]:
                values[cur_p - 1] = values[p_node - 1]
                Q.append(p_node)

        values[0] = value

    for query in queries:
        node, w = query
        if w == -1:
            answer.append(subtree(node))
        else:
            change_parent_node(node, w)

    return answer


v = [1,10,100,1000,10000]
e = [[1,2],[1,3],[2,4],[2,5]]
q = [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]
print(solution(v, e, q))