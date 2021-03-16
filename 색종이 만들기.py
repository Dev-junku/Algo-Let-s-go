N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

zero_cnt = 0
one_cnt = 0

def div(start_x, end_x, start_y, end_y):
    global arr, zero_cnt, one_cnt
    # if start_x == start_y:
    #     if arr[start_x][start_y] == 1:
    #         one_cnt += 1
    #         return
    #     else:
    #         zero_cnt += 1
    #         return
    n = ((end_x - start_x) + 1)**2
    one = 0
    zero = 0
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            if arr[i][j] == 1:
                one += 1
            else:
                zero += 1
    if one == n:
        one_cnt += 1
        return
    elif zero == n:
        zero_cnt += 1
        return
    div(start_x, (start_x+end_x)//2, (start_y+end_y)//2 + 1, end_y)
    div(start_x, (start_x+end_x)//2, start_y, (start_y+end_y)//2)
    div((start_x+end_x)//2+1, end_x, start_y, (start_y+end_y)//2)
    div((start_x+end_x)//2+1, end_x, (start_y+end_y)//2 + 1, end_y)

div(0, N-1, 0, N-1)

print(zero_cnt)
print(one_cnt)
