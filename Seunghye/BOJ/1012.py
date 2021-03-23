T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    # 저장
    ground = [[0 for _ in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y+1][x+1] = 1

    # 4방향 순회
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    count = 0
    for r in range(1, N+1):
        for c in range(1, M+1):
            # 배추 무리 발견시 BFS 수행
            if ground[r][c]:
                count += 1
                tovisit = [[r, c]]
                while tovisit:
                    i, j = tovisit.pop(0)
                    for idx in range(4):
                        if ground[i+dys[idx]][j+dxs[idx]]:
                            ground[i+dys[idx]][j+dxs[idx]] = 0
                            tovisit.append([i+dys[idx], j+dxs[idx]])
    print(count)
