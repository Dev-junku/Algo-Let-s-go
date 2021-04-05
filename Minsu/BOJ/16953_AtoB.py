def atob(A, B):
    # 걸린 횟수
    cnt = 1

    # A에서 B보다, B에서 A로 가는게 더 쉬울 것 같다.
    # 전 단계에서 2배를 곱했을 경우에는 짝수일 수 밖에 없다.
    while B > A:
        cnt += 1
        # 짝수라면
        if B % 2 == 0:
            # 2로 나눠주고
            B = B / 2

            # B가 A보다 작으면 실패, A와 같아지면 성공
            if B == A:
                return cnt
            elif B < A:
                return -1
        # 홀수라면
        else:
            # 끝 자리가 1이 아니라면
            if B % 10 != 1:
                return -1
            # 끝 자리가 1이면 10으로 나눈 몫
            else:
                B = B // 10

            # B가 A보다 작으면 실패, A와 같아지면 성공
            if B == A:
                return cnt
            elif B < A:
                return -1



A, B = map(int, input().split())


print(atob(A, B))


