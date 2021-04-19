# 틀린 풀이
# A, B = map(int, input().split())

# cnt = 0
# while B > A:
#     # print(B)
#     if B % 10 == 1:
#         B -= 1
#         B //= 10
#         cnt += 1
#     elif B % 2 == 0:
#         B //= 2
#         cnt += 1
        
# if B == A:
#     print(cnt+1)
# else:
#     print(-1)


from collections import deque
A, B = map(int, input().split())

que = deque([(A, 1)])
res = -1
while que:
    x, cnt = que.popleft()
    if x == B:
        res = cnt
        break

    if x*2 <= B:
        que.append((x*2, cnt+1))
    
    if int(str(x)+'1') <= B:
        que.append((int(str(x)+'1'), cnt+1))
    
print(res)