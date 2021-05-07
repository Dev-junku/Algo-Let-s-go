from heapq import heappush, heappop

def solution(jobs):

    '''
    초반에 필요한게 참 많아요..
    1. 현재 시점을 위한 (n)
    2. 최종 정답을 위한 (ans)
    3. jobs를 통제하기 위한 (i)
    '''

    ans, n, i = 0, 0, 0
    s = -1 

    '''
    4. heapq 쓸 부분
    '''
    h = []
    
    
    while i < len(jobs):

        '''
        5. 해당 시간에 있는 작업을 걸러야함.
        '''

        for j in jobs:
            if s < j[0] <= n:
                heappush(h, [j[1], j[0]])
        
                '''
                참고:
                위에 heappush(h, [j[1], j[0]])를 할 떄 일부러 앞 뒤를 뒤바꾸어 주었습니다.
                문제를 읽어보면 가장 짧은 대기 시간과 완료 시간으로 이야기 해서
                최대한 빨리 끝낼 수 있는 것을 위주로 끝내는 것이
                평균 완료 소요시간을 최소로 줄일 수 있는 걸 알 수 있어요.
                즉, 탐욕법으로 접근하지만, 자료 구조가 heap이거든요.
                다익스트라 푸셨을 때 heapq를 건드려보셨으면 아시겠지만,
                우선순위를 삽입할 때 처음 값을 기준으로 정렬되기 때문에
                요청시간과 걸리는 시간으로 주어진 자료를 걸리는 시간으로 정렬하기 위해서
                이 둘을 바꾸어서 정렬해줍니다.
                '''

        if len(h) > 0:
            c = heappop(h)
            s = n
            n += c[0]
            ans += (n - c[1])
            i += 1
        else:
            n += 1

    return int(ans/len(jobs))

if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))