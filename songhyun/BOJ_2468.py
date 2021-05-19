import sys
sys.stdin = open('input.txt')

move = [[-1, 0], [0, 1], [1, 0], [0, -1]] #상우하좌
def BFS(row, col, i):
    queue = [[row, col]]
    visited[row][col] = True
    while queue:
        cur = queue.pop(0)
        for idx in range(4):
            nr = cur[0] + move[idx][0]
            nc = cur[1] + move[idx][1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            else:
                if numbers[nr][nc] >= i and visited[nr][nc] == False:
                    queue += [[nr, nc]]
                    visited[nr][nc] = True
    return

N = int(input())
max_num = 0
numbers = [0] * N
num_list = []

max_cnt = 0
for idx in range(N):
    numbers[idx] = list(map(int, input().split()))
for row in range(N):
    for col in range(N):
        if numbers[row][col] not in num_list:
            num_list.append(numbers[row][col])
num_list.sort()
for i in num_list:
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(N):
            if numbers[row][col] >= i and visited[row][col] == False:           #안전영역이면 들어가서 안전영역 cnt
                BFS(row, col, i)
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
#코드를 줄이는 연습을 하자!

print(max_cnt)

#실수했던점 i를 visited를 True 만들며 처리하고 BFS를 돌리려고 했었으나 이럴경우 시간초과 나온다
#그래서 다시 visisted는 BFS가 while문을 빠져나올 수 있게만 만들고 여기에 탐색시 i보다 큰지 작은지
#판단하게 함으로써 시간 복잡도를 줄였다... 코드를 효율적으로 짜는 연습을 하자!!