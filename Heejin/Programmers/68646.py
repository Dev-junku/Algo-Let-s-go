# 작은걸 터트리는걸 최대 한 번만 할 수 있다.
def solution(a):
    answer = 2
    if len(a) <= 2:
        return answer

    left, right = a[0], a[-1]
    for i in range(1, len(a)-1):
        if left > a[i]:
            left = a[i]
            answer += 1
        if right > a[-1-i]:
            right = a[-1-i]
            answer += 1
    if left == right:
        answer -= 1
    return answer
