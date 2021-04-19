
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
one = 0

def div(x, y, N):
    global arr, minus, zero, one

    initial_v = arr[x][y] # 초기값

    dif = 0 # 재귀로 들어갈지 아니면 셀지
    for i in range(x, x+N):
        for j in range(y, y+N):
            if initial_v != arr[i][j]: # 다르면 바로 세워버림
                dif = 1
                k = N//3 # 범위 지정
                break
    
    if dif:
        div(x, y, k)
        div(x+k, y, k)
        div(x+2*k, y, k)

        div(x, y+k, k)
        div(x+k, y+k, k)
        div(x+2*k, y+k, k)

        div(x, y+2*k, k)
        div(x+k, y+2*k, k)
        div(x+2*k, y+2*k, k)
        return

    if initial_v == -1:
        minus += 1
    elif initial_v == 0:
        zero += 1
    else:
        one += 1
    return

div(0, 0, N)

print(minus)
print(zero)
print(one)





