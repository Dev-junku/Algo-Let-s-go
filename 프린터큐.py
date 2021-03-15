from sys import stdin
from collections import deque


T = int(stdin.readline().rstrip())

for t in range(1, T+1):
    print_list = deque()
    idx_list = deque()

    N, M = map(int, stdin.readline().rstrip().split())
    print_list.extend(list(map(int, stdin.readline().rstrip().split()))) 
    idx_list.extend([0] * N)
    idx_list[M] = 1
    cnt = 0
    while True:
        p_pri = print_list.popleft()
        p_idx = idx_list.popleft()
        cnt += 1
        if not print_list:
            break
        if p_pri < max(print_list):
            print_list.append(p_pri)
            idx_list.append(p_idx)
            cnt -= 1
        else:
            if p_idx == 1:
                break
    print(cnt)

