"""
문제설명 : 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
컨셉 : 1) DFS 구현 2) DFS가 돌아가는 횟수 계산
*주어진 인접행렬은 대칭이 아닙니다...
"""

def solution(n, computers):
    answer = 0
    visitied = [0] * n
    
    def dfs(v):
        visitied[v] = 1
        for i in range(n):
            if not visitied[i] and computers[v][i] == 1:
                dfs(i)

    for i in range(n):
        if not visitied[i]:
            answer += 1
            dfs(i)           

    return answer

print(solution(4, [[0] * 4 for _ in range(4)]))

# def dfs(v):
#     Q = [v]
#     while Q:
#         cur_n = Q.pop()
#         visitied[cur_n] = 1
#         computer = computers[cur_n]
#         for adj_n in computer[cur_n:]:
#             if adj_n == 1 and not visitied[adj_n]:
#                 Q.append(adj_n)