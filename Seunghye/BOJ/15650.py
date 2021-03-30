def backtrack(fr):
    # M개를 채웠으면 출력
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    # M개가 되지 못하고 N을 벗어나면 제외
    if fr > N:
        return
    # fr(범위 내 첫 수)부터 N까지, 해당 값을 수열에 추가하고 이후의 값 중에서 추가 투입
    for i in range(fr, N+1):
        sequence.append(i)
        backtrack(i+1)
        sequence.pop(-1)


N, M = map(int, input().split())
sequence = []
backtrack(1)
