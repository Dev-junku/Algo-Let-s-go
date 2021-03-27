from collections import Counter


def solution(clothes):
    cloth = []
    ans = 1
    for idx in range(len(clothes)):

        cloth.append(clothes[idx][1])

    cloth_Counter = Counter(cloth)

    for k in cloth_Counter.values():

        ans *= k+1
    return ans - 1

print(solution(clothes))