# board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]



def solution(board):
    result = 0
    def bfs(start):
        # inf 값을 더 신경써야겠다... 교훈 득템
        inf = 99999999999
        matrix = [[inf]*len(board) for _ in range(len(board))]
        matrix[0][0] = 0
        dys = [-1, 1, 0, 0]
        dxs = [0, 0, -1, 1]
        dirs = ['up', 'down', 'left', 'right']
        queue = []
        queue.append(start)
        while queue:
            y, x, cost, direction = queue.pop(0)

            for idx in range(4):
                dy, dx = dys[idx], dxs[idx]
                if dirs[idx] == direction:
                    tmp_cost = cost + 100
                else:
                    tmp_cost = cost + 600
                if 0 <= y + dy < len(board) and 0 <= x + dx < len(board) and board[y][x] == 0 and matrix[y+dy][x+dx] > tmp_cost:
                    matrix[y+dy][x+dx] = tmp_cost
                    queue.append([y+dy, x+dx, tmp_cost, dirs[idx]])
        return matrix[-1][-1]
    result = min(bfs([0, 0, 0, 'down']), bfs([0, 0, 0, 'right']))
    return result

# print(solution(board))