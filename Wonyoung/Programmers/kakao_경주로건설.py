
# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

from collections import deque


def solution(board):
    dc = [0, 0, 1, -1]
    dr = [1, -1, 0, 0]
    q = deque([])
    # 0. 좌표값과 방향 그리고 비용 초기값 할당
    q.append((0, 0, 0, 0))
    result = list([0]*len(board) for _ in range(len(board)))

    # 1. 우선순위 큐 실행
    while q:
        # 행 열 방향 비용 
        r, c, dir1, cost = q.popleft()
        # 우 좌 하 상
        for dir in range(4):
            nc = c + dc[dir]
            nr = r + dr[dir]

            if 0 <= nc < len(board) and 0 <= nr < len(board):
                if board[nc][nr] == 0:
                    if nc == 0 and nr == 0:
                        continue
                    # 첫 값 
                    if c == 0 and r == 0:
                        n_cost = cost + 100
                    # 직선도로인 값 
                    else:
                        if dir == dir1:
                            n_cost = cost + 100
                        # 500 + 100 코너와 직선1개
                        else:
                            n_cost = cost + 600
                    # 방문한 적이 없다면 q에 append
                    if result[nc][nr] == 0:
                        result[nc][nr] = n_cost
                        q.append((nr, nc, dir, n_cost))
                    # 기존 비용보다 지금 비용이 작다면 q에 append
                    else:
                        if result[nc][nr] >= n_cost:
                            result[nc][nr] = n_cost
                            q.append((nr, nc, dir, n_cost))
    # 2. 도착지의 최소 비용 출력 
    return result[-1][-1]
