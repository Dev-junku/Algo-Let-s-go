from sys import stdin


def count_color_range():
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                char = paint[i][j]  # 확인할 색
                visited[i][j] = True
                if char == 'B': # 파랑색인 경우 적록색맹에게도 개별적인 영역이 됨
                    count[1] += 1
                count[0] += 1

                tovisit = [(i, j)]
                while tovisit:
                    vi, vj = tovisit.pop()
                    for idx in range(4):
                        wi = vi + dis[idx]
                        wj = vj + djs[idx]
                        if 0 <= wi < N and 0 <= wj < N:  # 범위 이탈 방지
                            if paint[wi][wj] == char and not visited[wi][wj]:
                                visited[wi][wj] = True
                                tovisit.append((wi, wj))


def red_and_green():
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if paint[i][j] != 'B' and not visited[i][j]:
                visited[i][j] = True
                count[1] += 1
                tovisit = [(i, j)]
                while tovisit:
                    vi, vj = tovisit.pop()
                    for idx in range(4):
                        wi = vi + dis[idx]
                        wj = vj + djs[idx]
                        if 0 <= wi < N and 0 <= wj < N:  # 범위 이탈 방지
                            if paint[wi][wj] != 'B' and not visited[wi][wj]:
                                visited[wi][wj] = True
                                tovisit.append((wi, wj))


N = int(stdin.readline())
paint = [list(stdin.readline().rstrip()) for _ in range(N)]

count = [0, 0]

dis = [-1, 1, 0, 0]
djs = [0, 0, -1, 1]

red_and_green()     # 적록색약
count_color_range() # RGB

print('{} {}'.format(count[0], count[1]))