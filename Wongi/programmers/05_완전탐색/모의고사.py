def solution(answers):
    answer = [0] * 3

    person1 = [1, 2, 3, 4, 5]                   # 5
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]          # 8
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]    # 10
    i = 0
    while i < len(answers):
        number = answers[i]
        if person1[i % 5] == number:
            answer[0] += 1
        if person2[i % 8] == number:
            answer[1] += 1
        if person3[i % 10] == number:
            answer[2] += 1
        i += 1
    max_cnt = max(answer)

    result = []
    for i in range(3):
        if max_cnt == answer[i]:
            result.append(i+1)
    return result

answers = [1,2,3,4,5]
print(solution(answers))