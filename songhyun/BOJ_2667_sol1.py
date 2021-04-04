import sys
sys.stdin = open('input.txt')

move = [[-1,0], [0,1], [1,0], [0,-1]] # 상우하좌


def dfs(row, col):
    if row < 0 or row >= T or col < 0 or col >= T or numbers[row][col] != 1:          #여기서 인덱스 범위가 먼저들어가야
                                                                                      #인덱스 에러가 나지 않음!!
        return
    global cnt
    numbers[row][col] = 0 #무한루프에 빠지지 않게끔 돌려주기
    cnt += 1
    dfs(row - 1, col)  #상
    dfs(row, col + 1)  #우
    dfs(row + 1, col)  #하
    dfs(row, col - 1)  #좌
    return #다끝나고도 리턴



                          #for에 안결리면 즉 갈데가 없으면 cnt return



T = int(input())
matrix = [0]*T
cnt = 0
count = 0
for i in range(T):
    matrix[i] = input().split()
# print(matrix)
answer = []
numbers = [[0 for _ in range(T)]for _ in range(T)]
for row in range(T):
    for col in range(T):
        numbers[row][col] = int(matrix[row][0][col])

visited = [[False for _ in range(T)]for _ in range(T)]

for row in range(T):
    for col in range(T):
        if numbers[row][col] == 1:
            dfs(row, col)

            answer.append(cnt)
            cnt = 0
            count += 1


print(answer)

