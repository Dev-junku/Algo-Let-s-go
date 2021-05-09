import sys
sys.stdin = open('input.txt')

def binary(numbers):
    first = 1
    last = numbers[-1] - numbers[0] #최대 거리

    result = 0
    while first <= last:
        mid = (first + last) // 2
        cnt = 1
        new = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] >= mid + new:
                cnt += 1
                new = numbers[i]
        if cnt >= M:
            first = mid + 1

            result = mid
        else:
            last = mid - 1

    return result

N, M = map(int, input().split())
numbers = []
for _ in range(N):
    i = int(input())
    numbers.append(i)
numbers.sort()
# print(numbers)
print(binary(numbers))