from collections import deque

# 0은 빈 칸, 1은 벽
# N*N 정사각형 격자 부지. 0, 0에서 출발, N-1, N-1에 도착.
# 직선(상하/좌우연결) 100원, 코너(회전) 500원. 경주로 건설 최소 비용

def solution(board):
    N = len(board)
    INF = float('inf')
    min_cost = [[[INF, INF] for _ in range(N)] for _ in range(N)]   # 가로 진입, 세로 진입 비용 기록
        
    # 좌, 우, 상, 하
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    
    # 초기 출발점
    tovisit = deque()
    tovisit.append((0, 0))
    min_cost[0][0][0], min_cost[0][0][1] = 0, 0

    # 모든 방향 BFS -> 진입로 2개 방향(가로, 세로) 비용 기록
    while tovisit:
        vi, vj = tovisit.popleft()
        for d in range(4):
            wi, wj = vi + di[d], vj + dj[d]
            if 0 <= wi < N and 0 <= wj < N and not board[wi][wj]:   # 벽에 닿으면 이동 X
                # 이동 방향; 0은 가로, 1은 세로
                way = d // 2
                # 가로방향 이동: 가로방향(0) 최소값, (세로방향(1) 최소값 + 500) 중 작은 값 + 100으로 갱신, 다음 방문
                # 세로방향 이동: (가로방향(0) 최소값 + 500), 세로방향(1) 최소값 중 작은 값 + 100으로 갱신, 다음 방문
                new_cost = min(min_cost[vi][vj][way] + 100, min_cost[vi][vj][1-way] + 600)
                if new_cost < min_cost[wi][wj][way]:
                    min_cost[wi][wj][way] = new_cost
                    tovisit.append((wi, wj))
                    
    return min(min_cost[N-1][N-1])