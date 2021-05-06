def solution(phone_book):
    answer = True
    N = len(phone_book)

    for i in range(N):
        number = phone_book[i]
        length = len(number)
        for j in range(N):
            if i == j: continue
            compare_number = phone_book[j]
            if length > len(compare_number): continue
            if number == compare_number[:length]:
                answer = False
                return answer
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))


def solution(phone_book):
    answer = True
    N = len(phone_book)
    phone_book.sort()

    for i in range(0, N - 1):
        number = phone_book[i]
        next_nubmer = phone_book[i + 1]
        if len(number) > len(next_nubmer): continue
        if number == next_nubmer[:len(number)]:
            return False
    return answer

