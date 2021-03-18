def dq(x1, x2, y1, y2):
    size = x2 - x1
    # 파란색 색종이 수 확인
    blue = sum(sum(paper[i][x1:x2]) for i in range(y1, y2))
    if not blue:                # 하얀색 색종이
        count[0] += 1
    elif blue == (size ** 2):   # 파란색 색종이
        count[1] += 1
    else:                       # 섞여있는 경우 4분할
        size //= 2
        dq(x1, x1+size, y1, y1+size)
        dq(x1+size, x2, y1, y1+size)
        dq(x1, x1+size, y1+size, y2)
        dq(x1+size, x2, y1+size, y2)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
count = [0, 0]
dq(0, N, 0, N)

for i in range(2):
    print(count[i])
