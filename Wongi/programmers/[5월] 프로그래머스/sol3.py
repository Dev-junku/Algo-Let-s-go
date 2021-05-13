"""
x에 있는 "110"을 뽑아서, 임의의 위치에 다시 삽입합니다.
문자열 중 사전 순으로 가장 앞에 오는 문자열을 배열에 담아 return 하도록 solution 함수를 완성해주세요.



"""


# Time Over
# for문을 활용한 탐색은 빠르지 않음
# 그,, 문자열 탐색을 활용해야함...
def solution(s):
    answer = []

    def move_forward(x):
        front = rear = 0
        x = list(x)
        for i in range(len(x) - 2):
            if front and rear:
                break
            # 1. 뒤에서부터 110찾기
            if not rear and x[i * (-1) -1] == '0' and x[i * (-1) -2] == '1' and x[i * (-1) -3] == '1':
                rear = len(x) - 1 - i
            # 2. 앞에서부터 111찾기
            if not front and x[i] == '1' and x[i + 1] == '1' and x[i + 2] == '1':
                front = i + 2

        x[front], x[rear] = x[rear], x[front]
        return ''.join(x)

    def isTripleOne(x):
        for i in range(len(x) - 3):
            if x[i] == '1' and x[i + 1] == '1' and x[i + 2] == '1':
                return 1
        return 0


    for x in s:
        while isTripleOne(x):
            y = move_forward(x)
            if x == y:
                break
            x = y
        answer += [x]

    return answer


print(solution(["1110","100111100","0111111010"]))