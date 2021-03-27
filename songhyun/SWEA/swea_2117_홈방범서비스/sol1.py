import sys
from itertools import combinations
sys.stdin = open('sample_input (2).txt')

#BFS로 델타이동하면서 풀면될듯

def solution(N, M, row, col, k):
    queue = [[row, col]]
    cnt = 0
    while queue:
        cur = queue.pop(0)
        if matrix[cur[0]][cur[1]] == 1:
            cnt += 1
        if N % 2 == 1:
            if distance[cur[0]][cur[1]] == k+1:                         #앞에서 더해줬으므로 뻼
                return cnt - 1
        elif N % 2 == 0:
            if distance[cur[0]][cur[1]] == k:                         #앞에서 더해줬으므로 뻼
                return cnt - 1
        else:
            for i in range(4):
                nr = cur[0] + move[i][0]
                nc = cur[1] + move[i][1]                          #델타이동
                if nr < 0 or nr >= N or nc < 0 or nc >= N:        #인덱스 조건
                    continue
                else:
                    if distance[nr][nc] == 0:
                        distance[nr][nc] = distance[cur[0]][cur[1]] + 1        #현재행보다 + 1
                        queue += [[nr, nc]]                               #다음행 큐에 집어넣음과 동시에 distance1
    return cnt - 1

def check(cnt, M, k):
    cost = k * k + (k - 1) * (k - 1)
    return cost


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    matrix = [0] * N
    ans = []
    for idx in range(N):
        matrix[idx] = list(map(int, input().split()))
    # print(matrix)
    move = [[-1,0], [0,1], [1,0], [0,-1]]           #상우하좌 아.. 여기 좌표틀림 이거때매 계속 틀림...ㅠㅠㅠ
    for row in range(N):
        for col in range(N):
            for k in range(1, N):
                distance = [[0] * N for _ in range(N)]
                result = solution(N, M, row, col, k)
                result1 = check(result, M, k)
                if result1 == 0:
                    continue
                else:
                    ans.append(result1)

    print(max(ans))



