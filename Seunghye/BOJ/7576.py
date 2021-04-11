from sys import stdin

M, N = map(int, stdin.readline().split())
box = [[-1 for _ in range(M+2)]] + [[-1, *map(int, stdin.readline().split()), -1] for _ in range(N)] + [[-1 for _ in range(M+2)]]
left = M * N
tovisit = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if box[i][j]:
            if box[i][j] > 0:
                tovisit.append((i, j))
            else:
                left -= 1

if len(tovisit) == left:
    print(0)
else:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    while tovisit:
        count += 1
        temp = []
        for _ in range(len(tovisit)):
            vx, vy = tovisit.pop()
            left -= 1
            for idx in range(4):
                wx = vx + dx[idx]
                wy = vy + dy[idx]
                if not box[wx][wy]:
                    box[wx][wy] = 1
                    temp.append((wx, wy))
        tovisit = temp
    if left:
        print(-1)
    else:
        print(count - 1)
