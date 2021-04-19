N = int(input())


#### 이건 틀림

cnt = 0
n = int(N)
while n >= 10:
    n //= 10
    cnt += 1

end = 10**((cnt+1)//2)
start = 10**(cnt//2)

def bs(start, end):
    global N
    while True:
        mid = (start + end) // 2
        if mid ** 2 == N:
            return mid
        elif mid ** 2 > N:
            end = mid
        else:
            start = mid

print(bs(start, end))

#### 밑에는 맞음

def bs(start, end):
    global N
    while True:
        mid = (start + end) // 2
        if mid ** 2 == N:
            return mid
        elif mid ** 2 > N:
            end = mid
        else:
            start = mid

print(bs(0, N))

        
    

