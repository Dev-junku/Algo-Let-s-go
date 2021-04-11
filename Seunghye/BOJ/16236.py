from sys import stdin

N = int(stdin.readline())
space = [list(map(int, stdin.readline().split())) for _ in range(N)]

fish_size = 2           # 아기 상어 크기
fish_togo = fish_size   # 성장까지 남은 물고기 수
fish_in = [0, 0]        # 현재 위치
time = 0                # 소요 시간

# 아기 상어 시작 위치
find = False
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            fish_in = [i, j]
            space[i][j] = 0
            find = True
            break
    if find:
        break

# 델타: 상 좌 우 하
dis = [-1, 0, 0, 1]
djs = [0, -1, 1, 0]

keep_going = True
while keep_going:
    visited = [[0 for _ in range(N)] for _ in range(N)]     # 물고기 시작 위치별 방문기록
    visited[fish_in[0]][fish_in[1]] = 1
    can_eat = []                                            # 먹을 수 있는 물고기 목록

    # BFS로 가까운 곳 방문(visited[i][j] = 1)
    # 1초에 상하좌우 인접 1칸 이동
    tovisit = [fish_in]
    inner_time = 0                                          # 해당 지점까지 소요시간 계산
    while tovisit:
        # BFS 순회
        temp = []
        inner_time += 1
        for _ in range(len(tovisit)):
            vi, vj = tovisit.pop()
            for idx in range(4):
                wi = vi + dis[idx]
                wj = vj + djs[idx]
                # 범위 이탈 확인 및 최초 방문 기록
                if 0 <= wi < N and 0 <= wj < N and not visited[wi][wj]:
                    visited[wi][wj] = 1
                    # 먹을 수 있는 물고기면 (if space[i][j] < fish_size) 물고기 목록에 추가
                    if 0 < space[wi][wj] < fish_size:
                        can_eat.append([wi, wj])
                    # 먹을 수는 없지만 갈 수 있는 곳이면(if not 물고기 목록 and (not space[i][j] or space[i][j] == fish_size)) 다음 방문에 추가
                    elif not can_eat and (not space[wi][wj] or space[wi][wj] == fish_size):
                        temp.append([wi, wj])

        # 먹을 수 있는 물고기 발견시 순회 중단
        if can_eat:
            tovisit = []
            time += inner_time
            # 물고기 목록 정렬: i, j
            # 먹을 수 있는 가장 가까운(=지나야 하는 최소칸) + 가장 위/왼쪽 물고기
            i, j = sorted(can_eat, key=lambda x: (x[0], x[1]))[0]
            # 물고기 먹기 (fish_togo-=1)
            fish_in = [i, j]
            fish_togo -= 1
            space[i][j] = 0
            # 성장 (if not fish_togo: fish_size += 1 fish_togo = fish_size)
            if not fish_togo:
                fish_size += 1
                fish_togo = fish_size
        # 먹을 수 있는 물고기가 없다면 다음 칸 확인
        else:
            tovisit = temp

    # 모든 방문 가능한 곳을 확인해봤지만 더 먹을 수 없으면 종료
    if not can_eat:
        keep_going = False

print(time)
