import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
chk = [True,True] + [False for _ in range(N-1)]
numbers = []
ans = []
for idx in range(N+1):
    numbers.append(idx)
for idx in range(N+1):
    if chk[idx] == False:
        for j in range(2, N//numbers[idx]+1):      #전체에서 자기자신 나눈거만큼 그래야 끝까지 배수확인
            chk[numbers[idx]*j] = True

num = chk[M:N+1]
for idx in range(len(num)):
    if num[idx] == False:
        ans += [idx+M]
for num in ans:
    print(num)

