N = int(input())
roma_string = [1, 5, 10, 50]

s = set()

for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            l = N-i-j-k
            print(i, j, k, l)
            num = i + 5*j + 10*k + 50*l
            s.add(num)
print(len(s))









