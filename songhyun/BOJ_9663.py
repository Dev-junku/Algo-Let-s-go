import sys
sys.stdin = open('input.txt')


def tracking(queens):
    global cnt
    if len(queens) == N:
        cnt += 1
    else:
        for i in range(N):
            if i in queens:                      #수직
                continue
            for idx in range(len(queens)):
                if abs(i - queens[idx]) == len(queens) - idx:         #데각선
                    break
            else:                                 #break하면 else문 실행 x break문은 for문을 실행 안하게끔 하는것 뿐만아니라 반복문 끝내고 거기까지 코드를 중지
                queens.append(i)
                tracking(queens)
                queens.pop()                    #이게 백트래킹에 가장 중요한 코드 여기가 아니면 빼고 다시 트래킹
N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
# print(matrix)
for row in range(N):
    queens = []
    queens.append(row)
    tracking(queens)
print(cnt)
