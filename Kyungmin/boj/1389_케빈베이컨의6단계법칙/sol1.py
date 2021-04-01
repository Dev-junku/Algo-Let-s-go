import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
relation = [list(map(int, input().split())) for _ in range(M)]

# INF 는 무한대의 거리, 여기서는 100명 이내이므로 100이면 충분.
INF = 100

# 우선 NxN table 을 INF 로 채워넣는다.
table = [[INF] * N for _ in range(N)]

# 자기 자신의 경우 0을 넣는다.
for i in range(N):
    table[i][i] = 0

# table 에 relation 안의 관계들을 반영하여 연결된 경우 1을 넣는다.
for m in range(M):
    table[relation[m][0]-1][relation[m][1]-1] = 1
    table[relation[m][1]-1][relation[m][0]-1] = 1

# 플로이드-워셜 알고리즘 사용
for k in range(N):
    for y in range(N):
        for x in range(N):
            table[y][x] = min(table[y][x], table[y][k] + table[k][x])

# kevin 은 [케빈 베이컨 수, 사람 번호] 묶음들을 담는 2차원 리스트.
kevin = []
for i in range(N):
    kevin.append([sum(table[i]), i])

# 가장 작은 케빈 베이컨 수를 구한다.
tmp_min = 100
for people in kevin:
    if people[0] < tmp_min:
        tmp_min = people[0]

# 가장 작은 케빈 베이컨 수를 가진 사람을 번호가 적은 사람부터 찾는다.
for people in kevin:
    if people[0] == tmp_min:
        result = people[1] + 1
        # 만약 찾았다면, 번호가 가장 작은 사람을 구해야 하므로 break 한다.
        break
print(result)
