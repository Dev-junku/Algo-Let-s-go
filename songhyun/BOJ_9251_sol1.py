import sys
sys.stdin = open('input.txt')

set1 = list(input())
set2 = list(input())
answer = 0

dp = [[0 for _ in range(len(set1)+1)]for _ in range(len(set2)+1)]

for i in range(len(set1)):
    for j in range(len(set2)):
        if set1[i] == set2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            answer = max(dp[i+1][j+1], answer)
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(answer)
