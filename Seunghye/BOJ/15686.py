from copy import deepcopy

def backtrack(chicken):
    global minimum, c_count

    # 범위 이탈 방지
    if chicken == c_count:
        return

    # 포함하지 않는 부분집합
    backtrack(chicken+1)

    # 포함하는 부분집합
    available.append(chicken)
    subtotal = 0
    # 치킨집 모두 선택 완료 -> 거리 계산
    if len(available) == M:
        for c_dist in c_dists:
            subtotal += min(c_dist[i] for i in available)
            if subtotal > minimum:
                break
        else:
            if subtotal < minimum:
                minimum = subtotal
    # M개 미달인 경우 다음 단계
    else:
        backtrack(chicken+1)
    # 복구
    available.pop()


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 목록 만들기: 개별 치킨집은 2+i번으로 바꾸어서, 향후 치킨집 인덱스와 연결
chickens = []
c_count = 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
            city[i][j] += c_count
            c_count += 1

# 개별 집에서 모든 치킨집까지의 거리 확인
dis = [-1, 1, 0, 0]
djs = [0, 0, -1, 1]

c_dists = []                                        # 모든 집에서 모든 치킨집까지의 거리
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            c_dist = [0 for _ in range(c_count)]    # 개별 치킨집까지의 거리
            visit_city = deepcopy(city)             # 개별 집에서의 방문 배열
            tovisit = [(i, j)]                      # 방문할 칸
            visit_city[i][j] = -1                   # 출발지는 이미 방문한 것으로 기록
            distance = 0                            # 치킨거리

            while 0 in c_dist:                      # 미확인 치킨집이 없을 때까지
                temp = []                           # 다음 방문 칸
                distance += 1
                for _ in range(len(tovisit)):
                    vi, vj = tovisit.pop()
                    for d in range(4):
                        wi = vi + dis[d]
                        wj = vj + djs[d]
                        if 0 <= wi < N and 0 <= wj < N and visit_city[wi][wj] > -1:
                            # 치킨집이면 거리 저장
                            if visit_city[wi][wj] > 1:
                                c_dist[visit_city[wi][wj] - 2] = distance
                            visit_city[wi][wj] = -1  # 방문 기록
                            temp.append((wi, wj))    # 다음 방문지
                tovisit = temp
            c_dists.append(c_dist)

# 부분집합 만들기: M개까지의 부분집합을 만들고, 포함되는 치킨집만 확인한 개별 가정 최소 치킨거리 계산 후 누적합
minimum = N * N * len(c_dists)  # 이론적 최대 거리
available = []                  # 부분집합
backtrack(0)                    # 부분집합 만들기
print(minimum)                  # 최소값 출력
