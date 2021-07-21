cnt, n, nu = 0, 0, 0
set_combination = []

def dfs(empty ,N, user_id, banned_id):
    global cnt, n

    if N == n:
        empty = set(empty)
        if empty in set_combination:
            return
        set_combination.append(empty)
        cnt += 1
        return

    for i in range(nu):
        if user_id[i] in empty:
            continue

        if len(user_id[i]) != len(banned_id[N]):
            continue

        num = 0
        b_num = len(banned_id[N])
        for u, b in zip(list(user_id[i]), list(banned_id[N])):
            if b == '*':
                num += 1
                continue
            elif u == b:
                num += 1
            else:
                break

        if num == b_num:
            empty.append(user_id[i])
            dfs(empty, N + 1, user_id, banned_id)    
            empty.pop()


def solution(user_id, banned_id):
    global cnt, n, nu

    n = len(banned_id)
    nu = len(user_id)
    dfs([] ,0, user_id, banned_id)

    return cnt