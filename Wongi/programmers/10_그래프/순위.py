"""
선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 
정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

딕셔너리 배열 안에 set를 활용하여 선수들의 승부결과를 담습니다.

배운 점 : from collections import defaultdict

"""
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer

    
# from collections import defaultdict

def solution(n, results):
    answer = 0
    win = {i : set([]) for i in range(1, n + 1)}
    lose = {i : set([]) for i in range(1, n + 1)}
    # win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        w, l = result
        print(w, l)
        if not len(win.get(w)):
            win[w] = win.get(w, {l})
        else:
            win[w].add(l)

        if not lose.get(l, 0):
            lose[l] = lose.get(l, {w})
        else:
            lose[l].add(w)
        # lose[result[1]].add(result[0])
        # win[result[0]].add(result[1])
    print(win)
    print(lose)

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])    )
# def solution(n, results):
#     G = [[] * (n + 1) for _ in range(n + 1)]
#     parent = [[] * (n + 1) for _ in range(n + 1)]

#     for result in results:
#         v, w = result
#         G[v].append(w)
#         parent[w].append(v)

#     def dfs(v):
#         visited[v] = 1
#         for w in G[v]:
#             if not visited[w]:
#                 dfs(w)

#     player = []
#     for i in range(n + 1):
#         visited = [0] * (n + 1)
#         dfs(i)
#         if (len(parent[i]) + sum(visited)) == n:
#             print(i)
#             player += [i]
        

#     print(cnt)


            