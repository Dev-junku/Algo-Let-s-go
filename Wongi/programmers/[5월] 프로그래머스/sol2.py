"""
양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.

x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수

i.g.
f(2) = 3
"""

# 9/11 solved (-2 time over)
def solution(numbers):
    answer = []

    def itob(i):
        ans = ''
        while i:
            ans = str(i % 2) + ans
            i //= 2
        return ans

    def find_min_bit(number_bit):
        tmp = number
        while True:
            tmp += 1
            x = itob(tmp)
            cnt = len(x) - length
            for i in range(1, length + 1):
                if number_bit[-1 * i] != x[-1 * i]:
                    cnt += 1
                if cnt > 2:
                    break
            else:
                return tmp

    for number in numbers:
        number_bit = itob(number)
        length = len(number_bit)
        ans = find_min_bit(number_bit)
        answer += [ans]

    return answer

print(solution([2,7]))