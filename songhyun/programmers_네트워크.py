def solution(n, computers):
    com = [[] for _ in range(n + 1)]
    stack = []
    cnt = 0
    visited = [False for _ in range(n + 1)]
    for idx in range(n):  # 연결을 그래프로 만들기
        for num in range(n):
            if computers[idx][num] == 1:
                com[idx + 1] += [num + 1]

    for i in com:  # dfs 돌때마다 cnt + 1
        if len(i) > 0:
            cur = i.pop()
            if visited[cur] == False:
                stack = [cur]
                visited[cur] = True
                cnt += 1  # dfs 돌때마다 cnt + 1
                while stack:  # dfs
                    cur2 = stack.pop()
                    for i in com[cur2]:
                        if visited[i] == False:
                            visited[i] = True
                            stack.append(i)
    return cnt




computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

solution(computers, n)

