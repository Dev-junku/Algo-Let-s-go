N, M = map(int, input().split())
numbers = list(map(int, input().split()))
student = [0] * M
dp = [0]*(N+1)
total = 0
result = 0
for i in range(M):
        student[i] = list(map(int, input().split()))
for i in range(N):
        total += numbers[i]
        dp[i+1] = total
for i in range(M):
        result = dp[student[i][1]] - dp[student[i][0]-1]
        print(result / (student[i][1] - student[i][0] + 1))