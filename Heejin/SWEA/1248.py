def find(n, ans):
    if n > 0:
        ans.append(n)
        find(pa[n], ans)
    return ans


def preorder(n):
    if n > 0:
        visited[n] = 1
        preorder(left[n])
        preorder(right[n])


def find_same_par(n1_pas, n2_pas):
    for i in n1_pas:
        for j in n2_pas:
            if i == j:
                return i


T = int(input())
for tc in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    visited = [0] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    edges = list(map(int, input().split()))
    pa = [0] * (V + 1)
    for i in range(E):
        v1, v2 = edges[i * 2], edges[i * 2 + 1]
        if left[v1] == 0:
            left[v1] = v2
        else:
            right[v1] = v2
        pa[v2] = v1

    n1_pas = find(n1, [])
    n2_pas = find(n2, [])
    par = find_same_par(n1_pas, n2_pas)
    preorder(par)

    print("#{} {} {}".format(tc, par, sum(visited)))