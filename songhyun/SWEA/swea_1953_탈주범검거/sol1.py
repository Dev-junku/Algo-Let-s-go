import sys
sys.stdin = open('sample_input.txt')

def solution(row,col):
    queue = [numbers[row][col]]
    queue2 = [[row, col]]
    distance = [[0]*M for _ in range(N)]
    global H
    cnt = 0
    rear = 0
    distance[row][col] = 1
    while queue:
        cur = queue.pop(0)
        cur2 = queue2.pop(0)
        for i in directions[cur]:
            nr = cur2[0] + move[i][0]
            nc = cur2[1] + move[i][1]
            A = (i + 2) % 4
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            else:
                if A in directions[numbers[nr][nc]]:                      #이동할수 있으면
                    if distance[nr][nc] == 0:                             #방문체크
                        distance[nr][nc] = distance[cur2[0]][cur2[1]] + 1

                        queue.append(numbers[nr][nc])
                        queue2 += [[nr, nc]]                                  #queue2에 nr, nc넣음으로 방향과 queue 동시에 append로는 안넣어짐!
                        if distance[nr][nc] == H + 1:                         #
                            for row in range(N):
                                for col in range(M):
                                    if distance[row][col] != 0:
                                        cnt += 1

                            return cnt - 1                         #마지막에 들어간 하나 빼주기
    for row in range(N):
        for col in range(M):
            if distance[row][col] != 0:
                cnt += 1
    return cnt                                                 #여기는  걸리지 않고 나왔을때 ( H+1)이 되지 않았을때라서 +1

T = int(input())
for tc in range(1, 1+T):
    N, M, R, C, H = map(int,input().split())
    #N은 세로 M은 가로 R은 세로 시작위치 C는 가로시작위치, H는 시간
    numbers=[0]*N
    distance = [[0] * M for _ in range(N)]
    for idx in range(N):
        numbers[idx] = list(map(int,input().split()))
    directions = [[], [0,1,2,3], [0,2], [1,3], [0,1], [1,2], [2,3], [0,3]]    #0123 상우하좌
    move = [[-1,0],[0,1],[1,0],[0,-1]]       #상우하좌
    print('#{} {}'.format(tc,solution(R, C)))

