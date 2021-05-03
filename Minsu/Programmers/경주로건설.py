import time
start = time.time()

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]


def dfs(board, N, visited, y, x, lastDir, cost, dp):

    # 새로 기록된 cost가 더 크면 백트래킹
    if dp[y][x] < cost:
        return
    # 그렇지 않으면 해당 좌표에 새로운 cost 할당하고 진행
    else:
        dp[y][x] = cost

    # 기존 종료조건
    if y == x == N-1:
        return
    
    # 델타이동할 값
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위에 속하고, 벽이 아니고, 방문하지 않았다면
        if 0 <= ny < N and 0 <= nx < N and not board[ny][nx] and not visited[ny][nx]:
            # 방문처리
            visited[ny][nx] = 1

            # 첫 시작이라면 비용에 1을 더해줌
            if y == 0 and x == 0:
                dfs(board, N, visited, ny, nx, i, cost+100, dp)
            # 방향이 다르다면 (코너)
            elif lastDir != i:
                dfs(board, N, visited, ny, nx, i, cost+600, dp)
            # 방향이 같다면
            else:
                dfs(board, N, visited, ny, nx, i, cost+100, dp)

            # 방문기록 초기화
            visited[ny][nx] = False



def solution(board):
    N = len(board)  # 한 변의 길이
    INF = float('inf')  # 양의 무한대를 나타내는 표현
    dp = [[INF for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문기록

    dfs(board, N, visited, 0, 0, 0, 0, dp)

    return dp[N-1][N-1]


print(solution(board))

print(time.time()-start)
