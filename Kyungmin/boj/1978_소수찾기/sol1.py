import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
result = 0

# 약수의 개수가 2개면 소수
for num in nums:
    # 약수의 개수 (나누어 떨어지는 횟수) 를 담을 임시 변수
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    # 약수가 2개면 결과 + 1
    if cnt == 2:
        result += 1
print(result)