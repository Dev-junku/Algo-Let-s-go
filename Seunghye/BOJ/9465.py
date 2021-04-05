from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    stickers = [list(map(int, stdin.readline().split())) for _ in range(2)]
    stickers.append([0 for _ in range(n)])

    # 각 열별 스티커 선택: 0행, 1행, 떼지 않기(2행)
    # 이 때, 이전 단계에서 선택 가능한 옵션(자기 행을 제외한 행) 중 가장 큰 누적점수를 선택하여 합
    for i in range(1, n):
        stickers[0][i] += max(stickers[1][i-1], stickers[2][i-1])
        stickers[1][i] += max(stickers[0][i-1], stickers[2][i-1])
        stickers[2][i] += max(stickers[0][i-1], stickers[1][i-1])

    # 마지막 열을 기준으로 가장 높은 누적합을 출력
    print(max(stickers[i][n-1] for i in range(3)))
