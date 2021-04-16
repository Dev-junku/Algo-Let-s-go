def inorder(tree, a, node):
    global sum_, count_
    # 자식 노드이면, 음, 양수 구분해서 리턴해줘
    if len(tree[node]) == 0:
        count_ += abs(a[node])
        return a[node] * -1
    else:
        value = 0
        for ch in tree[node]:
            value += (inorder(tree, a, ch) * -1)
            # 부모에 있던 값이랑 합
        sum_ = (a[node] + value)
        count_ += abs(sum_)
        return sum_ * -1


sum_ = 0
count_ = 0

def solution(a, edges):
    root_flag = False
    result = 0
    root = 0
    tree = [[] for _ in range(len(a))]
    graph = [[] for _ in range(len(a))]
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    for i in range(len(graph)):
        # 개수가 1이 아니면 무조건 부모임.
        # i 가 부모라고 했을 때 자식들.
        if len(graph[i]) != 1:
            if not root_flag:
                root = i
                root_flag = True
            # 루트로 정해진 부모가, 있으면 지우고, 자식으로 트리 구성해줘
            if root in graph[i]:
                graph[i].remove(root)
            tree[i] += graph[i]
    result = inorder(tree, a, root)
    if result != 0:
        result = -1
    else:
        result = count_

    return result

print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))