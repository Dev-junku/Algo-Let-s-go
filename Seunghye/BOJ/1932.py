N = int(input())
# 수월한 이전 단계 확인을 위해 0, 0으로 감쌈
triangle = [[0, *map(int, input().split()), 0] for _ in range(N)]

maximum = 0
for i in range(1, len(triangle)):
    for j in range(1, i+2):
        # 이전 단계까지의 누적합 중 큰 것을 합산
        triangle[i][j] += max((triangle[i-1][j-1], triangle[i-1][j]))
        # 마지막 층에서 가장 큰 수 확인
        if i == len(triangle) - 1 and maximum < triangle[i][j]:
            maximum = triangle[i][j]

print(maximum)
