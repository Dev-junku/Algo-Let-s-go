import sys
sys.stdin = open('input.txt')

def add(mid):
    cnt = 0
    sum_num = 0
    for i in numbers:
        if sum_num + i > mid:     #이부분 중요 더하면 mid값 넘어가면 cnt 하고 초기화
            cnt += 1
            sum_num = 0
        sum_num += i
    if sum_num:
        cnt += 1
    return cnt

N, count = map(int, input().split())
numbers = list(map(int, input().split()))

# print(numbers)

right = sum(numbers)
left = max(numbers)


while left <= right:
    mid = (left + right)//2
    cnt = add(mid)
    if cnt <= count:
        right = mid - 1
    else:
        left = mid + 1
print(left)
