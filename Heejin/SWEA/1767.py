import sys
sys.stdin = open("sample_input (1).txt")
from copy import deepcopy
from pprint import pprint

def dfs(processors,pro_visited, p_idx, length):
    global min
    global visited
    global max_processors
    # 만약 마지막 프로세서까지 길이 조정을 끝냈다면 length를 반환한다.
    if len(processors) == p_idx:
        # pprint(visited)
        sum_visited = sum(pro_visited)
        # 코어갯수 가장 많은것.
        if max_processors < sum_visited:
            max_processors = sum_visited
            min = length
        # 코어 갯수가 현재 방문된 코어랑 같다면, 그 다음으로 적은 전선 체
        elif max_processors == sum_visited:
            if min > length:
                min = length

        return min
    # 현재 프로세서의 좌표값을 안다.
    current = processors[p_idx]
    cur_col = current[0]
    cur_row = current[1]

    dy = [ -1, 1, 0, 0, 0]
    dx = [ 0, 0, 1, -1, 0]

    for d_idx in range(5):
        new_col = cur_col
        new_row = cur_row
        count = 0  # 이번 프로세서에서 dy, dx 방향으로 갈 때 길이
        # 만약에 얘가 움직이지 못하는 코어라면?
        # 바로 다음 dfs로 넘어가야해. 이 코어는 visited가 False인채로
        if dy[d_idx] == dx[d_idx] == 0:
            dfs(processors, pro_visited, p_idx+1, length + count)

        else:
            while 0 <= new_col < N and 0 <= new_row < N:
                new_col = new_col + dy[d_idx]
                new_row = new_row + dx[d_idx]
                count += 1

                if visited[new_col][new_row] == 1: # 전선을 만났어
                    break # 이번 라인은 아니다. 하고 다음 방향으로 넘어가.


                # while문을 다 돌았다는 거는 길이 있다는거니까 여기서 dfs 한번 넣어주고 다음 d_idx로 가게됌.
                if (d_idx == 0 and new_col == 0) or (d_idx == 1 and new_col == N-1) or (
                        d_idx == 2 and new_row == N-1) or (d_idx == 3 and new_row == 0):
                    # 전선을 깔
                    col = cur_col
                    row = cur_row
                    for _ in range(count):
                        col = col + dy[d_idx]
                        row = row + dx[d_idx]
                        visited[col][row] = 1
                    # pprint(visited)
                    # 다음으로 가.
                    pro_visited[p_idx] = True
                    dfs(processors,pro_visited, p_idx+1, length + count)
                    pro_visited[p_idx] = False
                    # 나와서 다시 복구
                    # print('dfs 후 복')
                    col = new_col
                    row = new_row
                    for _ in range(count):
                        visited[col][row] = 0
                        col = col + (dy[d_idx] * -1)
                        row = row + (dx[d_idx] * -1)

                    # pprint(visited)
                    break


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split(' '))) for i in range(N)]
    processors = []
    min = 987654321
    max_processors = 0
    p_count = 0
    # (col, row) 형식으로 저장해놓음. 각 반도체의 좌표를.
    for i in range(1, N-1):
        for j in range(1, N-1):
            if matrix[i][j] == 1:
                processors.append((i, j))

    visited = matrix
    pro_visited = [False for _ in range(len(processors))] # 이미 방문된 코어 저장하기.
    dfs(processors, pro_visited, 0, 0)
    print("#{} {}".format(tc, min))