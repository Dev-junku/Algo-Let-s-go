def solution(left, right):
    odd_list= [i * i for i in range(1, 32)]

    answer = sum(list(range(left, right + 1)))
    for number in range(left, right + 1):
        if number in odd_list:
            answer -= (number * 2)

    return answer