import sys; sys.stdin = open('input.txt', 'r')

# 섬의 개수를 세시오
# try1 : RuntimeError T.T
def numIsland(grid):
    def dfs(i, j):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid[0]) or \
        grid[i][j] != 1:
            return
        
        grid[i][j] = 0
        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i + 1, j + 1)
        dfs(i - 1, j + 1)
        dfs(i + 1, j - 1)
        dfs(i - 1, j - 1)
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
                
    return count

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    print(numIsland(grid))