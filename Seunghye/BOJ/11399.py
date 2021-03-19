N = int(input())
P = sorted(map(int, input().split()))
for i in range(1, N):
    P[i] += P[i-1]
print(sum(P))