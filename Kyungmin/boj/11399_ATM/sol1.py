import sys
sys.stdin = open('input.txt')

N = int(input())
times = list(map(int, input().split()))

times.sort()
result = 0
for i in range(len(times)):
    result += times[i]*(len(times)-i)
print(result)
