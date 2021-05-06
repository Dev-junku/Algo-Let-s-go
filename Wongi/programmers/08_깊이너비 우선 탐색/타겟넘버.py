"""
문제 설명 : 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성
컨셉 : 1) 순열의 합을 구합니다 2) 순열의 합이 target 숫자와 같은 경우를 구합니다.

"""

answer = 0
def solution(numbers, target):
    N = len(numbers)
    bits = [0] * N
    if sum(numbers) < target:
        return 0

    # 
    def backtrack(k):
        global answer
        if k == N:
            total = 0
            for i in range(N):
                if bits[i]:
                    total -= numbers[i]
                else:
                    total += numbers[i]
            if total == target:
                answer += 1 

        else:
            bits[k] = 0
            backtrack(k + 1)
            bits[k] = 1
            backtrack(k + 1)

    backtrack(0)
    return answer

"""
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    while queue:
        s, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))

    return answer
"""

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))