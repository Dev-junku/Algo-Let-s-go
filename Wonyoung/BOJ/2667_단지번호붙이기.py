# import sys
# sys.stdin = open('input.txt')

from collections import deque


# 3. 지도 범위 내인지 확인
def is_safe(c, r):
    if 0 <= c < n and 0 <= r < n:
        return 1
    else:
        return 0


# 2. deque는 queue 보다 찾는 속도가 빠르다 양끝에 원소가 있을때 걸리는 시간복잡도가 n 이아니라 1임.
def bfs(c, r, idx):
    # 이중리스트로 감싸주어야 아래 node가 리스트 식으로 나와 node[i]에서 c와 r값을 꺼낼 수 있다.
    q = deque([[c, r]])
    visited[c][r] = 1

    while q:
        # 선입선출
        node = q.popleft()
        # 상하좌우로 살펴줌
        for dir in range(4):
            nc = node[0] + dc[dir]
            nr = node[1] + dr[dir]
            # 범위내에 있고 방문한적없고 1이라면 queue에 삽입
            if is_safe(nc, nr):
                if smap[nc][nr] == 1 and visited[nc][nr] == 0:
                    q.append([nc, nr])
                    # 방문체크
                    visited[nc][nr] = 1
                    # 크기 증가
                    house[idx] += 1


# T = int(input())
# for tc in range(1, T+1):
n = int(input())
# 0. n*n 지도
smap = [list(map(int, input())) for _ in range(n)]
# 방문을 체크해줄 리스트
visited = [[0]*n for _ in range(n)]
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
# 키 벨류값을 담을 딕셔너리
house = {}
idx = 0
# 1. 순회를 돌며 방문하지 않았고 값이 1인 원소들을 찾음
for i in range(n):
    for j in range(n):
        if smap[i][j] and visited[i][j] == 0:
            # 딕셔너리에 0번부터 벨류값의 초기치를 1로하고
            house[idx] = 1
            # 2. bfs 함수를 돌며 1을 추가로 발견할 때 마다 값을 더함
            bfs(i, j, idx)
            # 키 값 이동
            idx += 1

# 4. 오름차순 정렬해야함 (이거 안해서 계속 틀림)
house = sorted(house.values())
# 5. 길이와 집단크기 오름차순으로 출력
print(len(house))
for i in house:
    print(i)