from sys import stdin
from copy import deepcopy

N = int(stdin.readline())
original = [[0 for _ in range(N+2)]] + [[0, *map(int, stdin.readline().split()), 0] for _ in range(N)] + [[0 for _ in range(N+2)]]

maximum = 1     # 물 높이가 최저치보다 낮을 때
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for water in range(min(min(original[i]) for i in range(1, N+1)), max(max(original[i]) for i in range(1, N+1))):
    count = 0                               # 안전 지역의 수
    temp_map = deepcopy(original)           # 기록을 위해 deepcopy하여 사용
    # 전체 영역 순회
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 안전 지역 BFS
            if temp_map[i][j] > water:
                tovisit = [(i, j)]
                count += 1
                while tovisit:
                    vi, vj = tovisit.pop(0)
                    for d in range(4):
                        wi = vi + delta[d][0]
                        wj = vj + delta[d][1]
                        # 안전 지역이라면 다음 탐색에 추가
                        if temp_map[wi][wj] > water:
                            tovisit.append((wi, wj))
                            temp_map[wi][wj] = water
    if count > maximum:
        maximum = count

print(maximum)
