# 1. 능력치 차이의 최소를 찾는 함수 실행
def solution(idx, cnt):
    global smallest
    # n까지 오면 인덱스 초과
    if idx == n:
        return
    # 반으로 팀이 나뉘었을 때 팀별 스탯의 차를 구함
    if cnt == n//2:
        s1, s2 = 0, 0
        for i in range(n):
            for j in range(n):
                # 1으로 된 팀
                if check[i] and check[j]:
                    s1 += stat[i][j]
                # 0으로 된 팀
                elif not check[i] and not check[j]:
                    s2 += stat[i][j]
        # 기존보다 작으면 최소값 갱신
        if smallest > abs(s1-s2):
            smallest = abs(s1-s2)
        return

    # 선택
    check[idx] = 1
    # 다음값 탐색
    solution(idx+1, cnt+1)
    # 탐색 후 리셋
    check[idx] = 0
    # 다음 인덱스를 선택하기 위해서 인덱스만 올려주기
    solution(idx+1, cnt)


# n명의 선수
n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
# 팀을 구분하기 위한 리스트
check = [0]*n
smallest = 9999
# 1. 능력치 차이의 최소를 찾는 함수 실행
solution(0, 0)
# 2. 결과값 출력
print(smallest)