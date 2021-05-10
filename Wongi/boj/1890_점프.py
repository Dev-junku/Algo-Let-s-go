import sys; sys.setrecursionlimit(1500)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
visited[-1][-1] = 1

def dp(r, c):
    if visited[r][c] < 0:
        visited[r][c] = 0
        move = arr[r][c]
        if r + move < N:
            visited[r][c] += dp(r + move, c)
        if c + move < N:
            visited[r][c] += dp(r, c + move)
    return visited[r][c]

dp(0, 0)
print(visited[0][0])


# sol3. dfs
# memo = [[0] * N for _ in range(N)]
# cnt = 0
# def dfs(r, c):
#     if r == N -1 and c == N - 1:
#         return 1

#     if memo[r][c] == 0:
#         move = arr[r][c]
#         if 0 <= r + move < N and 0 <= c < N:
#             memo[r][c] += dfs(r + move, c)
#         if 0 <= r < N and 0 <= c + move < N:
#             memo[r][c] += dfs(r, c + move)
#     return memo[r][c]

# print(dfs(0, 0))



# 2. visited sol - Wrong Ans
# visited = [[0] * 101 for _ in range(101)]
# def dyn(r, c):
#     global cnt
#     if r == N -1 and c == N - 1:
#         cnt += 1
#         return

#     if r >= N or c >= N or arr[r][c] == 0:
#         return

#     if not visited[r][c]:
#         visited[r][c] = 1
#         move = arr[r][c]
#         dyn(r + move, c)
#         dyn(r, c + move)

# dyn(0, 0)
# print(cnt)



# # 1. just recursive - OverTime
# def solution(r, c):
#     global cnt
#     if 0 > r or r >= N or 0 > c or c >= N:
#         return

#     if r == N - 1 and c == N - 1:
#         cnt += 1
#         return

#     move = arr[r][c]
#     if move == 0:
#         return
#     solution(r + move, c)
#     solution(r, c + move)

# solution(0, 0)
# print(cnt)