import sys

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(10)]
paper_num = [0] * 5
res = sys.maxsize


def BackTracking(x, y, cnt):
    global res

    if y >= 10:
        res = min(res, cnt)
        return

    if x >= 10:
        BackTracking(0, y+1, cnt)
        return
    
    if arr[x][y]:
        for num in range(5):
            if paper_num[num] == 5:
                continue

            if x + num >= 10 or y + num >= 10:
                continue

            whether = 0
            for i in range(x, x+num+1):
                for j in range(y, y+num+1):
                    if arr[i][j] == 0:
                        whether = 1
                        break
                if whether:
                    break
            
            if not whether:
                for i in range(x, x+num+1):
                    for j in range(y, y+num+1):
                        arr[i][j] = 0
                
                paper_num[num] += 1
                BackTracking(x+num, y, cnt+1)
                paper_num[num] -= 1

                for i in range(x, x+num+1):
                    for j in range(y, y+num+1):
                        arr[i][j] = 1

    else:
        BackTracking(x+1, y, cnt)

BackTracking(0, 0, 0)

if res == sys.maxsize:
    print(-1)
else:
    print(res)
