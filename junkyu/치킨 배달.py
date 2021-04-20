N, M = map(int, input().split())

chic_map = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

distance = 987654321

for i in range(N):
    for j in range(N):
        if chic_map[i][j] == 2:
            chicken.append((i, j))
        elif chic_map[i][j] == 1:
            house.append((i, j))

def combinations(N_list, M):
    result = []

    if M == 0:
        return [[]]
    
    for i in range(len(N_list)):
        element = N_list[i]
        N_ele = N_list[i+1:]
        for j in combinations(N_ele, M-1):
            result.append([element]+j)
    
    return result

for chic in combinations(chicken, M):
    total = 0
    for h in house:
        total += min([abs(h[1] - c[1]) + abs(h[0] - c[0]) for c in chic])
        if distance < total:
            break
    if total < distance:
        distance = total

print(distance)
            