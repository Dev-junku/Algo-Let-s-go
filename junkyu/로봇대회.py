import sys

sys.stdin = open('문제3_input.txt')

# 일반적인 bfs
def bfs(now_x, now_y):

    dist = [[-1] * N for _ in range(N)]
    q = [(now_x, now_y)]
    dist[now_x][now_y] = 0

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] == -1 and arr[nx][ny] != 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

# 갈 곳을 찾자
def find(dist, loc):

    for l in loc: # 일단 거리를 추가
        l.insert(0, dist[l[0]][l[1]])
    
    # 최소값을 찾아서 소팅해야함.
    min_v = loc[0][0] # 초깃값
    for i in range(len(loc)):
        for j in range(i, len(loc)):
            if min_v > loc[j][0]: # 소팅
                min_v = loc[j][0] # 거리를 기준으로
                loc[i], loc[j] = loc[j], loc[i] # 소팅이다!

    # 처음 부분만 뽑자. (거리, 좌표값 저장되어 있음)
    value = loc.pop(0) 
    # 나머지를 다시 리스트로 만들자. 있음.
    loc_copy = [[loc[i][1], loc[i][2]] for i in range(len(loc))] 
    
    return value, loc_copy

# 델타 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


T = int(input())

res = 0
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
   
    # 존의 좌표를 전부 넣어줌
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                now_x, now_y = i, j
            elif arr[i][j] == 3:
                red_x, red_y = i, j
            elif arr[i][j] == 4:
                green_x, green_y = i, j
            elif arr[i][j] == 5:
                blue_x, blue_y = i, j

    # 존의 좌표만 뽑자.
    loc = [[red_x, red_y], [green_x, green_y], [blue_x, blue_y]]

    # 어차피 존은 3개만 나오니까 3번만 반복하자.
    i = 3
    # 결과를 저장할 res
    res = 0 
    while i > 0:
        # 일단 존 가면 못감 그래서 1로 저장
        arr[now_x][now_y] = 1
        # bfs랑 위치 찾아서 거리 더하기!
        value, loc = find(bfs(now_x, now_y), loc)
        # 좌표값 갱신
        now_x, now_y = value[1], value[2]
        # 거리값 더하기
        res += value[0]
        if not loc: # loc이 더이상 없으면 강제 종료
            break

    print(f'{t} {res}')