from collections import deque

N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def safe(x, y): # 안전한지 확인
    if x >= N or x < 0 or y >= N or y < 0: # 이 조건을 만족시키면 아웃오브사이드
        return False # 안돼~
    return True # 돼~


start_point = [] # 시작 점을 모으기
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0: # 시작 점만 따로 모으자
            start_point.append((arr[i][j], 0, i, j)) # 이 때 중요한게 그 값, 시작 시간(0초), 위치(i, j)

start_point.sort() # 소팅하면 arr[i][j]를 기준으로 소팅 됨
queue = deque(start_point) # 이거 queue에 추가

def bfs(): # bfs 실시
    global s # 이건 바이러스 전파되는 시간이니까 전역으로 잡고 
    while queue: # queue 따 쓸 때까지 가자
        location, second, cx, cy = queue.popleft() # 일단 꺼내자.
        if s == second: # 만약에 문제에서 지정한 초와 현재 초가 같다면
            break # 묻고 따지지 말고 끝내자.
        for i in range(4): # 이게 안 되면
            nx, ny = cx + dx[i], cy + dy[i] # 델타 이동으로 새로운 x,y를 잡고
            if safe(nx, ny): # 안전한지 검사
                if arr[nx][ny] == 0: # 거기에 0까지 맞다면
                    arr[nx][ny] = location # 이 부분은 바이러스가 전염됨(중요한건 처음에 sorting에서 작은 수 순으로 감염됨)
                    queue.append((arr[nx][ny], second+1, nx, ny)) # 이거 queue에 추가
bfs() # bfs 실시
print(arr[x-1][y-1]) # 좌표 값 하나씩 빼주고 출력
                



    

