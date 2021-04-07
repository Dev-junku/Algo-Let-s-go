def solution(s):
    round = 0
    zero_count = 0
    while s != "1":
        round += 1
        zero_count += s.count("0")
        s = s.replace("0","")
        new_num = len(s)
        s = bin(new_num)[2:]
    answer = [round, zero_count]
    return answer


## 아래는 첫 번째 풀이입니당.
## 마지막 세 개 테케에서 시간초과 났습니다 ㅠㅠ
## 연산이 많다고 생각했습니다!

# def remove_zero(s):
#     global zero_count
#     s = list(s)
#     while '0' in s:
#         zero_count += 1
#         s.remove('0')
#     return s
#
#
# def make_binary(num):
#     if num > 0:
#         q = num // 2
#         r = str(num % 2)
#         return make_binary(q)+r
#     return ""
#
#
# zero_count = 0
#
#
# def solution(s):
#     round = 0
#     while int(s) > 1:
#         round += 1
#         s_without_zero = ''.join(remove_zero(s))
#         new_num = len(s_without_zero)
#         s = make_binary(new_num)
#     answer = [round, zero_count]
#     return answer