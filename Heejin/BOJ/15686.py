import sys
sys.stdin = open('input.txt')


def get_house_chicken_dist(idxs):
    all_dist = 0 # 총 거리 더할 변수
    # 집 별로 최소 거리를 구할거기 때문에 집을 순회
    for i, house in enumerate(houses):
        house_dist = 0
        # M개의 치킨집 좌표 부분집합 순회
        for idx in idxs:
            chicken = chickens[idx]
            # 거리
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            # 거리가 0 이거나 현재거리보다 더 가깝다면 갱신
            if house_dist == 0 or house_dist > dist:
                house_dist = dist
        # 한 집이 끝났다면 그 집과 치킨집의 최소거리를 합산.
        all_dist += house_dist

    return all_dist


N, M = map(int, input().split())
area = [list(map(int,input().split())) for _ in range(N)]

# 집이랑 치킨집 좌표 저장하기
houses, chickens = [], []
for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            houses.append((i, j))
        elif area[i][j] == 2:
            chickens.append((i, j))

# 부분집합 구하기. bit로.
N = len(chickens)
min_distance = 99999
for i in range(1 << N):
    idxs = []
    for j in range(N):
        if i & (1 << j):
            idxs.append(j)
            if len(idxs) > M:
                break
    if len(idxs) == M:
        # 주어진 조건 개수만큼 부분집합이 만들어졌으면,
        dist = get_house_chicken_dist(idxs)
        if dist < min_distance:
            min_distance = dist

print(min_distance)
