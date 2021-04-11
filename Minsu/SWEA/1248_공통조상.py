import sys
sys.stdin = open('input.txt')

# 전위순회 함수
def preorder(n, visited):
    if 1 <= n <= V:
        visited[n] = 1
        preorder(left[n], visited)
        preorder(right[n], visited)

    # A와 B를 자식으로 갖는다면 리턴값을 가지게 된다.
    if visited[A] == 1 and visited[B] == 1:
        count = 0
        for i in range(len(visited)):
            if visited[i] == 1:
                count += 1
        return n, count


T = int(input())
for tc in range(1, T+1):
    V, E ,A, B = map(int, input().split())
    edges = list(map(int, input().split()))
    left = [0] * (V + 1) # 왼쪽자식을 담는 리스트
    right = [0] * (V + 1) # 오른쪽자식을 담는 리스트
    pa = [0] * (V + 1) # 자식의 인덱스에 부모를 담는 리스트

    for i in range(E):
        if left[edges[2*i]] == 0:
            left[edges[2*i]] = edges[2*i+1]
        else:
            right[edges[2*i]] = edges[2*i+1]
        pa[edges[2*i+1]] = edges[2*i]

    # visited = [0] * (V + 1)  # 방문기록을 담는 리스트
    # print(preorder(5, visited))

    x = A
    visited = [0] * (V + 1)  # 방문기록을 담는 리스트
    # A의 부모, 그 부모의 부모 순으로 전위순회하면서 A와 B를 자식으로 갖는 노드를 찾는다.
    while True:
        if preorder(pa[x], visited) is None:
            x = pa[x]
        else:
            result = preorder(pa[x], visited)
            print('#{} {} {}'.format(tc, result[0], result[1]))
            break


