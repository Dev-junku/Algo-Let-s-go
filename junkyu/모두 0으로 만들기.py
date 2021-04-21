'''
setrecursionlimit 재귀 함수의 최대 깊이 디폴트값을 바꾸는 것.
'''

import sys
sys.setrecursionlimit(300000)

'''
programmers의 경우 백준과는 다르게 함수만 작성하는 느낌이라
전역 변수를 어떻게 다뤄야할지 정말 고민이 많았는데,
진짜 단순했음. 함수 사이에 이를 연결해주고 싶으면
그냥 모든 함수에 global 작성하고 해당 변수를 입력하면 그만..
'''

def dfs(idx, a, board):
    global visited, answer, N
    
    '''
    초기 시작하는 idx는 0임
    a는 특정 노드에 값이 기록된 값이고
    board는 인접 리스트
    '''

    '''
    일단 현재는 들어온 0은 인덱스 그 자체임
    이를 방문처리함
    '''

    now = a[idx]
    visited[idx] = 1

    '''
    그리고 해당 인덱스 부분을 방문하지 않았으면 dfs를 돌리면 그만
    '''

    for i in board[idx]:
        if visited[i] == 0:
            now += dfs(i, a, board)
    
    '''
    몇 번만에 가능하지 물어보았으므로
    연산을 수행하는 것 자체가 count를 하는 것.
    따라서 해당 수치를 절대값으로 바꾼 다음에 더해주어야함.
    '''
    answer += abs(now)

    '''
    now를 리턴해서 now에 더한다는게 좀 이해가 안 될 수 있는 데
    이게 출력되는 now와 34번 째 줄의 now는 다른 값임
    왜냐하면 재귀로 돌려서 나오는거니까
    즉 25번 째 줄에서 새로운 now를 할당하니까다른 것임.
    '''


    return now


def solution(a, edges):
    global visited, answer, N

    '''
    노드에 기록 숫자의 합이 0이 아니면 절대 문제의 조건을 만족시킬 수 없으므로
    합한 값이 0인지 확인
    '''

    if sum(a) != 0:
        return -1
    
    answer = 0

    '''
    이제 이를 통해서 인접 리스트로 만들어야 하는 데,
    중요한건 그래프에 있어서 방향성이 따로 존재하지 않는다는 점
    그래서 무모가 무엇이고 자식이 무엇인지? 이러한 고민을 하게 되는데
    진짜 단순한게 이거 그냥 뒤바꿔서 인접 리스트에 저장하면 되었음..
    '''

    N = len(a)
    board = [[] for _ in range(N)]

    for i, j in edges:
        board[i].append(j)
        board[j].append(i)
    
    '''
    방문기록을 남길 리스트를 만들어주기
    '''

    visited = [0] * N 

    '''
    이제 dfs로 깊이 우선 탐색을 시작!
    '''

    dfs(0, a, board)

    return answer

'''
한 줄 평: 우리가 배운 것에 너무 한정적으로 접근하면 문제 접근을 못할 수 있음.. ㅜㅠ
'''

## 테스트 케이스 돌리는 코드
if '__main__' == __name__:
    print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
    print(solution([0,1,0], [[0,1],[1,2]]))