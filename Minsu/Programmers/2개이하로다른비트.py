numbers = [2, 7]


def solution(numbers):
    answer = []

    for number in numbers:

        number_str = '0' + format(number, 'b')  # 이진수 문자열로 변환

        # 오른쪽에서부터 가장 첫번째 0을 찾음
        for i in range(len(number_str)-1, -1, -1):
            if number_str[i] == '0':
                # 첫번째 자리부터 0이 나왔다면 끝자리를 1로 교체
                if i == len(number_str)-1:
                    result = number_str[:-1] + '1'
                # 첫번째 자리가 1이라면 가장 먼저 만나는 01을 10으로 교체
                else:
                    result = number_str[0:i] + '10' + number_str[i+2:len(number_str)]
                break

        result = int(result, 2)  # 다시 10진수로 변환
        answer.append(result)

    return answer


print(solution(numbers))
