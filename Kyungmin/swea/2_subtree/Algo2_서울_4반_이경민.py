# subtree 는 해당 노드를 루트로 하는 서브트리의 크기를 구하는 함수
def subtree(node):
    # 전역 변수인 cnt 값을 변경하기 위해 global 사용
    global cnt
    # subtree 함수가 호출될 때 마다 cnt 값을 1 더해준다.
    cnt += 1
    # tree[node] 는 node 의 자식들을 담은 리스트
    # 자식이 없다면 건너뛰게 된다.
    for new_node in tree[node]:
        # 재귀 호출
        subtree(new_node)


T = int(input())
for tc in range(1, T+1):
    # V = 노드의 개수, N = 목표 노드 번호
    V, N = map(int, input().split())
    # info = 노드 쌍에 대한 정보
    info = list(map(int, input().split()))
    # 0번 인덱스를 제외하므로 노드의 개수 +1 개 만큼 만든다.
    tree = [[] for _ in range(V+1)]

    # 인덱스 = 노드 번호, 값 = 각 노드 번호의 자식 이 되도록 넣어준다.
    # 노드 쌍의 개수만큼 순회
    for i in range(V-1):
        parent, child = info[i*2:(i+1)*2]
        tree[parent].append(child)

    cnt = 0
    subtree(N)
    # N번 노드의 자손 노드 개수는, N번 노드를 루트로 하는 서브트리의 개수에서
    # 자기 자신을 빼 준 값과 같다.
    # 결과 출력
    print('#{} {}'.format(tc, cnt - 1))
