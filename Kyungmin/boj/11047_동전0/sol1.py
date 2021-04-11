import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# 순회 편의를 위해 내림차순으로 뒤집기
coins = list(reversed(coins))
result = 0
i = 0
# 금액이 0이 될때까지 while 순회
while K:
    # 현재 동전의 가치가 현재 금액보다 크거나 같은 동안 순회
    while coins[i] <= K:
        result += 1
        K -= coins[i]
    i += 1
print(result)
