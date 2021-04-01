import sys
sys.stdin = open('input.txt')

n = int(input())
a, b = map(int, input().split())
m = int(input())
relation = [list(map(int, input().split())) for _ in range(m)]

INF = 100
table = [[INF] * n for _ in range(n)]

for i in range(n):
    table[i][i] = 0

for i in range(m):
    table[relation[i][0]-1][relation[i][1]-1] = 1
    table[relation[i][1]-1][relation[i][0]-1] = 1

# 플로이드 와샬 알고리즘 사용
for k in range(n):
    for y in range(n):
        for x in range(n):
            table[y][x] = min(table[y][x], table[y][k] + table[k][x])

# 만약 INF 라면 -1로 변경
for y in range(n):
    for x in range(n):
        if table[y][x] == INF:
            table[y][x] = -1

# 인덱스는 0부터 시작하므로 1을 빼서 출력
print(table[a-1][b-1])
