from sys import stdin

# 새로운 연산자가 나와야 누적된 피연산자 바탕의 연산 가능
# -> i 뒤에 올 연산자를 정하고, i를 피연산자에 추가하여 연산하고, 그 결과를 다음에 전달
# -> i == N인 경우, i를 피연산자에 추가하여 연산하고, 그 결과가 0이면 [수식] + [i]를 출력
# 수식: [기존수식] + [i] + [새로운 연산자]
def backtrack(N, i, sub_total, next_operator, next_operand, string):
    if i == N:
        if next_operator == '+' and not sub_total + int(next_operand + str(i)):
            print(string + str(i))
        elif next_operator == '-' and not sub_total - int(next_operand + str(i)):
            print(string + str(i))
    else:
        # ' '
        backtrack(N, i+1, sub_total, next_operator, next_operand + str(i), string + str(i) + ' ')

        if next_operator == '+':
            sub_total += int(next_operand + str(i))
        else:
            sub_total -= int(next_operand + str(i))
        # '+'
        backtrack(N, i+1, sub_total, '+', '0', string + str(i) + '+')
        # '-'
        backtrack(N, i+1, sub_total, '-', '0', string + str(i) + '-')


T = int(stdin.readline())
for tc in range(T):
    N = int(stdin.readline())
    backtrack(N, 1, 0, '+', '0', '')
    if tc < T-1:
        print()
