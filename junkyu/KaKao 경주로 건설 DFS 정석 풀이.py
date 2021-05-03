# 출처: https://yjios.tistory.com/43

'''
문제 푸는 알고리즘이 대표적으로 2가지

1. DFS
2. BFS

2번의 경우 풀이를 찾아보니까. 저희 스터디에서 푼 코드가
가독성이며, 코드 길이이며 더 좋아서 딱히 다른 풀이가 필요없는거 같아
DFS만 찾았습니다.

일단 해당 풀이의 아이디어는 저와 동일하며 더 작은 cost가 나왔을 때는 업데이트하고
그렇지 않았을 때는 return 하여 재귀를 멈추는 BackTracking 방식을 채택한 점입니다.
물론 시간복잡도는 BFS보다 훨씬 높지만, 그래도 해당 풀이로 푸는것도 좋은 풀이 중 하나로 생각드네요.

아래 코드는 업데이트를 위해 dp라는 2차원 배열을 새로 만들어줬습니다.
이를 통해 하나씩 cost를 기록해주면서 dfs를 기록할거에요

우선 answer를 무한대로 할당하고 이를 res와 비교할 겁니다.

일단 필요한 parameter는 엄청 많은데,

코드를 조금 더 가꾸면, 많은 부분이 사라질거에요.
아직 이렇게 안해봤지만, 아마 될거 같습니다.

parameter 설명

board: 벽부분을 피하기 위해서 사용
n: 범위 벗어나는 부분을 피하기 위해 사용
visited: 이미 방문한 부분은 피하기 위해 사용
y, x: 좌표 확인 및 이동을 위해 사용
lastDir: 비용, 100원인지 600원인지 확인하기 위해 사용, (방향이 바뀌었는지)
res: 비용을 기록하면서 쓸모없는 dfs는 return하기 위해 사용
dp: res를 차례로 기록하면서 최종 답을 내리기 위해 사용

총 8개의 parameter가 DFS 함수에서 재귀적으로 돌아가게 되는데, 이거 잘 쫒아오시면 되겠습니다.

쉬운 해설을 위해 주석에 기입한 번호를 따라서 코드를 리뷰하시면 금방 해당 코드를 이해할 수 있을겁니다.
'''


import sys
sys.setrecursionlimit(10**9)

answer = float('inf')


def dfs(board,n,visited,y,x,lastDir,res,dp) :

    '''
    3.  res는 dp라는 2차원 배열에 총비용/100으로만 기록됩니다.
        이 코드에서는 마지막에 100을 곱해서 답을 도출합니다.
    '''


    '''
    4.  dp값이 res보다 작으면 return
        이미 기록된 cost가 새로 기록된 cost보다 더 작단 의미임
        그렇지 않으면 res 해당 좌표에 res를 할당

        그리고 만약에 좌표값이 n-1, n-1 끝 값이면 그냥 끝
    '''
    if dp[y][x] < res :
        return
    else :
        dp[y][x] = res

    if y == n-1 and x == n-1 :
        return

    
    '''
    델타 이동을 위한 direction
    이를 그대로 lastDir과 확인할 겁니다.
    참고로 lastDir은 처음에 0으로 들어옵니다.
    물론 어떤 숫자로 들어와도 답을 도출하는데는 상관없습니다.
    '''
    d = [[0,1],[0,-1],[1,0],[-1,0]]

    for i in range(4) :
        ny = y + d[i][0]
        nx = x + d[i][1]

        '''
        5.  안전한지 확인하기!
            이를 위해 다음을 확인합니다.
            -1 생성된 ny, nx가 범위 안에 있는지
            -2 board에 0이 기록되어 있는지(갈 수 있는지)
            -3 방문을 했었는지(불필요한 방문인지)

            확인해야합니다. 만약에 이 3개 중 하나라도 만족되지 않는다면
            dfs를 돌 수 없겠죠 그리고 이 3개의 조건으로 인해 무한재귀에 빠지지 않게 되죠
        '''
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0 and not visited[ny][nx] :
            '''
            6. 조건에 맞다면 일단 방문처리합니다.
            '''
            visited[ny][nx] = True
            '''
            7.  첫 시작이라면 그냥 바로 다음 stage로 옮기는데 res에 1만 더합니다.
                즉, 비용이 100 오른거에요
                그렇지 않고 lastDir과 i가 다르면, 즉 방향이 다르면
                6을 방향이 같다면 1을 res에 더해줍니다.
            '''
            if y == 0 and x == 0 :
                dfs(board, n, visited, ny, nx, i, res+1, dp)
            elif lastDir != i :
                dfs(board, n, visited, ny, nx, i, res+6, dp)
            else:
                dfs(board, n, visited, ny, nx, i, res+1, dp)
            visited[ny][nx] = False
            
            '''
            8.  하나의 i에 대해 재귀가 끝났다면 visited를 False로 돌려서
                다른 방향을 고려할 수 있게 해줍니다.
            '''


def solution(board):
    global answer

    '''
    1. DFS를 돌리기 위한 parameter 생성
    '''

    n = len(board)
    INF = float('inf')
    dp = [[INF for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    '''
    2. 시작!
    '''
    dfs(board,n,visited,0,0,0,0,dp)

    '''
    9.  최종적으로 dp[n-1][n-1]에 남는건 최소의 res 값이며 100곱해서
        solution함수에서 반환하면 정답을 출력할 수 있습니다.
    '''
    return dp[n-1][n-1]*100


if __name__ == '__main__':
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
    print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
    print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))