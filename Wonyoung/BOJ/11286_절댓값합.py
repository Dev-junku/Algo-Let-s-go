import heapq
from sys import stdin
# sys.stdin = open('input.txt')


# T = int(input())
# q = []
# for _ in range(T):
#     num = int(input())
#     if num != 0:
#         heapq.heappush(q, (abs(num), num))
#     else:
#         if q:
#             print(heapq.heappop(q)[1])
#         else:
#             print(0)


# SWEA 처럼 불러오지 않기 
T = int(stdin.readline().rstrip())
q = []
for _ in range(T):
    num = int(stdin.readline().rstrip())
    # 0일 때 값이 있다면 작은 순으로 빼오고 없다면 0출력
    if not num:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    # 절대값을 기준으로 push하기 
    else:
        heapq.heappush(q, (abs(num), num))

