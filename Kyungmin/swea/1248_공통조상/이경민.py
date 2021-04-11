import sys
sys.stdin = open('input.txt')


# 부모를 구하는 함수
def parent(a):
    return tree[a][2]


# 서브트리의 크기를 구하는 함수
def subtree(a):
    global size
    for i in range(2):
        if tree[a][i]:
            size += 1
            subtree(tree[a][i])


T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    my_list = list(map(int, input().split()))
    # tree 는 [자식1, 자식2, 부모] 를 요소로 하는 이차원 리스트
    tree = [[0] * 3 for _ in range(V+1)]

    # 자식1, 자식2 채우기
    for i in range(len(my_list)):
        if not i % 2:
            if not tree[my_list[i]][0]:
                tree[my_list[i]][0] = my_list[i+1]
            else:
                tree[my_list[i]][1] = my_list[i+1]
    # 부모 채우기
    for i in range(len(tree)):
        if tree[i][0]:
            tree[tree[i][0]][2] = i
        if tree[i][1]:
            tree[tree[i][1]][2] = i

    # 각각 A의 조상들, B의 조상들, 공통 조상들
    parent_A = []
    parent_B = []
    commons = []
    A_ = A
    B_ = B
    while parent(A):
        parent_A.append(parent(A))
        A = parent(A)
        if A == 1:
            break
    while parent(B):
        parent_B.append(parent(B))
        B = parent(B)
        if B == 1:
            break
    for n in parent_A:
        if n in parent_B:
            commons.append(n)
    # 가장 가까운 공통 조상
    common = max(commons)
    size = 1
    subtree(common)
    print('#{} {} {}'.format(tc, common, size))
