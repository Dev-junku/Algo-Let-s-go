"""
문제 설명 : 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
컨셉 : 1) Stack 2) 뒤에서부터 꺼내어 앞의 수와 비교합니다.

"""

def solution(prices):
    # prices의 길이는 2이상 100000 이하입니다.
    N = len(prices)
    answer = [0] * N
    stack = []

    for i in range(N):
        price = prices[i]

        # stack이 비어있다면 stack에 넣기
        # (i, price)
        if not stack:
            stack.append((i, price))

        else:
            # stack top과 비교하여, price보다 크다면 꺼내기
            while stack and price < stack[-1][1]:
                idx, _ = stack.pop()
                answer[idx] += (i - idx)
            stack += [(i, price)]

    for s in stack:
        idx, _ = s
        answer[idx] = (N - 1 - idx)

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))