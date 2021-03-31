def solution(string):

    # 왼쪽 괄호를 위한 스택
    left = []

    for char in string:
        # 왼쪽 괄호일때
        if char in ['(', '[']:
            left.append(char)
        # 오른쪽 괄호일때
        elif char in [')', ']']:
            # 왼쪽 괄호가 남아있지 않으면 no 리턴
            if len(left) == 0:
                return 'no'
            elif char == ')': 
                if left[-1] == '(':
                    left.pop()
                else:
                    return 'no'
            elif char == ']':
                if left[-1] == '[':
                    left.pop()
                else:
                    return 'no'

    # left의 길이가 0이면 yes, 그렇지 않으면 no 리턴
    if len(left):
        return 'no'
    else:
        return 'yes'


while True:
    string = input()

    # 종료조건
    if string == '.':
        break

    print(solution(string))

            
