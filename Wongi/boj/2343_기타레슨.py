import sys; sys.stdin=open('2343.txt', 'r')

"""
이분 탐색

left : 최소 블루레이 크기 (max of arr)
right : 최대 블루레이 크기 (sum of arr)
mid : (left + right) // 2

1) 만약 블루레이의 개수가 부족하다면 right = mid - 1
2) 만약 블루레이의 개수가 초과하다면 left = mid + 1

reference : https://deok2kim.tistory.com/109
"""

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def solution():
    cnt = 0
    total = 0
    for i in range(N):
        if total + arr[i] > mid:
            cnt += 1
            total = 0
        total += arr[i]
    else:
        if total:
            cnt += 1
    return cnt

right = sum(arr)
left = max(arr)
while left <= right:
    mid = (right + left) // 2
    cnt = solution()
    print(cnt)
    if cnt <= M:
        right = mid - 1
    elif cnt > M:
        left = mid + 1

print(left)

