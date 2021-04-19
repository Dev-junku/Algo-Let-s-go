from collections import deque

INF = 1e9 # 상어와 먹이의 거리에 대한 초깃값

#### 데이터 입력 받는 부분 ####

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

#############################

shark_size = 2 # 초기 상어 사이즈


# 상어 위치 찾고 배열에 0으로 만들기!
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            now_x, now_y = i, j 
            arr[now_x][now_y] = 0

# 델타 이동 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs로 상업와 먹이 사이의 최단거리를 구하는 것이 포인트
def bfs():
    # 거리 배열을 만듬 -1을 초깃값으로 설정한 이유는 44번째 줄에서 거르기 위함임.
    dist = [[-1] * n for _ in range(n)]

    # 일반적인 queue 설정
    queue = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0 # 시작 값은 위에서 구했으니, 대입해서 0으로 만듬 왜냐면 거리는 0이기 때문

    # bfs 시작
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and arr[nx][ny] <= shark_size:
                    dist[nx][ny] = dist[x][y] + 1 # 44번째 줄의 조건이 만족되면 그 값에서 1씩 더해가면서 거리를 계산함.
                    queue.append((nx, ny))

    return dist


# 먹이 찾기!
def find(dist): # bfs에서 구한 거리 배열을 매개변수로 설정!
    x, y = 0, 0
    # 최소 거리를 설정, 최대한 큰 값으로 설정하기 위해서 3번째 줄에서 10억이라는 숫자를 할당.
    min_dist = INF
    # 순회 시작
    for i in range(n): # 이 부분이 '거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기를 먹습니다.'에 해당!
        for j in range(n):
            # 거리가 -1이라는 의미는 가지 못한다는 의미, 물고기의 사이즈는 상어의 크기보다 작아야하고 1보다는 크거나 같아야 함.
            if dist[i][j] != -1 and 1 <= arr[i][j] < shark_size: 
                # 해당 거리가 최소 길이보다 작으면
                if dist[i][j] < min_dist:
                    # x, y를 설정 -> 이걸 왜 설정하냐면 return값으로 먹이의 위치를 반환 할 것이기 때문에
                    x, y = i, j
                    # 그리고 최소 거리도 반환하기 위해 해당 먹이가 있는 거리를 min_dist에 저장.
                    min_dist = dist[i][j] 
    # 만약에 min_dist가 계속 10억이면, 그냥 None을 반환
    if min_dist == INF: 
        return None
    else: # 그렇지 않다면
        return x, y, min_dist # 물고기의 위치와 최소 거리를 반환
    
res = 0 # 최종 결과값을 담을 객체
ate = 0 # 먹은 횟수를 담을 객체

# 반복구문 시작!
while True:
    # bfs를 돌리면 현재 상어의 위치에서 먹이까지의 최소 거리를 담은 배열이 반환되고
    # find를 돌리면 최소거리를 매개변수로 현재 상어의 위치와 먹이까지의 최소 거리(얘는 배열이 아님)가 반환됨
    value = find(bfs())
    # 만약에 None이면, 즉 68번 줄의 조건을 만족시켜서 최소 거리가 10억이면
    if value == None: 
        print(res) # res를 반환 처음에 먹을게 없으면 자동으로 0임
        break
    else: # 그렇지 않다면
        now_x, now_y = value[0], value[1] # x, y(먹이의 위치)
        res += value[2] # 현재 상어의 위치에서 먹이의 거리(거리가 결국 시간임..)를 더함

        arr[now_x][now_y] = 0 # 그 먹이를 0으로 다시 할당
        ate += 1 # 먹었기 때문에 ate에 1을 더하기

        if ate >= shark_size: # 상어 크기보다 더 많이 먹었으면
            shark_size += 1 # 사이즈 1 키우기
            ate = 0 # 먹은건 초기화