import sys

sys.stdin = open('input.txt')

T = int(input())

def bfs(n):
    global left, right

    if n > 0:
        bfs(left[n])
        bfs(right[n])
        if not visited[n]:
            visited[n] = 1

        return


for t in range(1, T+1):
    # 정점 총 수, 간선의 총 수, 공통 조상 찾기 위한 정점 번호
    V, E, n1, n2 = map(int, input().split()) # 정점번호 중 누굴 택해서 돌려야할까?

    left = [0 for _ in range(V+1)]
    right = [0 for _ in range(V+1)]
    # 트리 정점 정보 받기
    node_list = list(map(int, input().split()))

    # 간선 정보 입력
    for i in range(len(node_list)//2):
        N1, N2 = node_list[i*2], node_list[i*2+1]
        if left[N1] == 0:
            left[N1] = N2
        else:
            right[N1] = N2


    i = 1
    start_node = 1
    node_num = V
    while i < V:
        visited = [0 for _ in range(V + 1)]
        bfs(i)
        i += 1
        if visited[n1] != 1 or visited[n2] != 1:
            continue

        s = sum(visited)
        if visited[n1] == 1 and visited[n2] == 1 and s <= node_num:
            start_node = i
            node_num = s

    print('#{} {} {}'.format(t, start_node-1, node_num))