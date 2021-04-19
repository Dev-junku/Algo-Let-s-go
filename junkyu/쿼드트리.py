N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]
res = ''

def div(start_x, end_x, start_y, end_y):
    global arr, res
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
        res += '1'
        return
        
    if zero == n:
        res += '0'
        return
        
    res += '('
    div(start_x, (start_x+end_x)//2, start_y, (start_y+end_y)//2)
    div(start_x, (start_x+end_x)//2, (start_y+end_y)//2 + 1, end_y)
    div((start_x+end_x)//2+1, end_x, start_y, (start_y+end_y)//2)
    div((start_x+end_x)//2+1, end_x, (start_y+end_y)//2 + 1, end_y)
    res += ')'

div(0, N-1, 0, N-1)
print(res)