def solution(brown, yellow):
    answer = []
    LW = (brown - 4) // 2

    for y in range(1, yellow // 2 + 1):
        q, r = divmod(yellow, y)
        if r == 0:
            if q + y == LW:
                answer.extend([q+2, y+2])
                break
    else:
        answer.extend([LW+1, LW+1])
    return answer

print(solution(8, 1))