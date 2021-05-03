# 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 요금
graph = []
INF = int(1e9)

def dfs(x, y, cost, direcx, direcy, N):
    global res
    # print(x, y)

    # 이거 없으면 무한 루프 돌아서 해줘야합니다.
    # 아래 조건이면 더이상 dfs를 할 이유가 없죠
    if graph[x][y] < cost:
        return

    # INF이면 cost로 바꿔줍니다.
    if graph[x][y] == INF:
        graph[x][y] = cost

    # 만약에 cost가 더 작으면, 바뀌준다. 여기서 N-1, N-1 인덱스이면 멈춰!
    if graph[x][y] > cost:
        graph[x][y] = cost
        if x == N-1 and y == N-1:
            return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 일단 안전한지 확인해야함.
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > 1:
            # 시작이면 100원 추가
            if direcx == 0 and direcy == 0:
                # 재귀 돌려!
                dfs(nx, ny, cost+100, dx[i], dy[i], N)
            else:
                # 그렇지 않으면, 처음시작도 아니면서
                # 방향이 바뀌었으면
                if direcx != dx[i] or direcy != dy[i]:
                    # 600원 추가
                    dfs(nx, ny, cost+500+100, dx[i], dy[i], N)
                else:
                    # 그렇지 않고 같은 방향이면 100원 추가
                    dfs(nx, ny, cost+100, dx[i], dy[i], N)
                        

def solution(board):
    global graph
    answer = 0
    N = len(board)
    graph = board
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                graph[i][j] = INF
    dfs(0, 0, 0, 0, 0, N)
    return graph[N-1][N-1]


if __name__ == '__main__':
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
    print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
    print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))