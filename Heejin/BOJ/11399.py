N = int(input())
times = list(map(int, input().split()))

total = 0
times.sort()
for i in range(N):
    total += times[i] * (N-i)

print(total)