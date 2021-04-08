import sys
sys.stdin = open('input1.txt')

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 순회를 위한 델타
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

# 아기상어의 초기 위치 저장 후 0으로 변경
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

# 생각한 풀이 방법
# 1. 자기보다 작은 물고기 찾기
# 2. 그 중에서 도달 가능하고, 가장 가까운 물고기 찾기
# 3. 거리가 같은 물고기가 여러 개라면 가장 위, 가장 왼쪽 물고기 우선
# 4. 먹었다면, 먹은 당시의 시간 저장
# 5. 먹은 횟수가 자기 자신의 크기와 같다면, 크기 + 1, 먹은 횟수 초기화
# 6. 현재 위치를 기준으로 1~5를 더 이상 먹을 수 없을 때까지 반복
# 7. 반복 종료시의 시간 출력
