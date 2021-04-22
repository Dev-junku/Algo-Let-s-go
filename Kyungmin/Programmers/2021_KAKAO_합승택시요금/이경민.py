def solution(n, s, a, b, fares):
    # 초기 정답 = 가능한 최대값
    answer = 100001 * 201
    # 행렬 inf 값으로 초기화
    matrix = [[100001] * (n + 1) for _ in range(n + 1)]
    # x, y 값이 같으면 0으로
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if y == x:
                matrix[y][x] = 0
    # 요금 값 (가중치) 를 넣는다.
    for fare in fares:
        matrix[fare[0]][fare[1]] = fare[2]
        matrix[fare[1]][fare[0]] = fare[2]
    # 플로이드-워셜 알고리즘 적용
    for k in range(n+1):
        for y in range(n+1):
            for x in range(n+1):
                matrix[y][x] = min(matrix[y][x], matrix[y][k] + matrix[k][x])
    # 브루트 포스
    # 기존 정답과 [시작점 s에서 i까지 동승하고, i부터 각각 따로 간 금액들의 합]을 비교해
    # 더 작은 것을 정답에 넣는다
    for i in range(n+1):
        answer = min(answer, matrix[s][i] + matrix[i][a] + matrix[i][b])
    return answer


n, s, a, b = 7, 3, 4, 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

print(solution(n, s, a, b, fares))
