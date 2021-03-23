N, r, c = map(int, input().split())

size = 2 ** N       # 방문 범위의 한 변 크기
num_start = 0       # 방문 순서 범위의 시작
index_start_r = 0   # 방문 범위의 시작 r
index_start_c = 0   # 방문 범위의 시작 c

# 분할 정복
# 4분의 1 구역 중 해당되는 범위 확인: 가로, 세로 -> 해당 기준에 맞춰 출발(현재 크기/4*i), 도착(현재 크기/4*i+1) 입력
# 크기가 1이 되면 그 때 숫자를 return
while size > 1:
    size //= 2      # 4분할
    quarter = [True for _ in range(4)]  # 세부 분할면 결정: 0 1 / 2 3

    # 가로 범위 이탈 제외
    if r < index_start_r+size:
        quarter[2], quarter[3] = False, False
    else:
        quarter[0], quarter[1] = False, False
        index_start_r += size   # 아래쪽 영역이므로 다음 시작 범위 변경

    # 세로 범위 이탈 제외
    if c < index_start_c+size:
        quarter[1], quarter[3] = False, False
    else:
        quarter[0], quarter[2] = False, False
        index_start_c += size   # 오른쪽 영역이므로 다음 시작 범위 변경

    # 방문 순서 시작수 변경
    num_start += (size ** 2 * [i for i in range(4) if quarter[i]][0])

print(num_start)
