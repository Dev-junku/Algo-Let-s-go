def find(N, K):
    queue = [N]
    visited = [[False] * 500001 for _ in range(2)]
    flag = 0
    sec = 0
    visited[0][N] = True

    # queue를 돌면서
    while queue:
        # 동생이 500000을 넘어가면 끝내고
        if K > 500000:
            break
        # 동생이 방문한 시간에 이미 수빈이가 방문했던 곳이면 수빈이도 동생이 방문한 시간에 다시 방문 가능한 것.
        # 2초를 주기로 그 위치로 다시 돌아올 수 있기 때문이다.
        # 초 반환.
        if visited[flag][K]:
            return sec

        tmp = []
        # 짝 홀 판단.
        flag = 1 - flag
        # queue의 한 단계(sec)을 돌면서
        for n in queue:
            # 3가지 방법을 순회하면서
            for next in [n-1, n+1, n*2]:
                # 조건에 맞으면 수빈이가 방문했다고 체크 및 tmp에 추가해줌.
                if 0 <= next <= 500000 and not visited[flag][next]:
                    visited[flag][next] = True
                    tmp.append(next)
        # sec, 동생 길이, queue를 업데이트해줌.
        sec += 1
        K += sec
        queue = tmp
    return -1

N, K = map(int, input().split())

print(find(N, K))


