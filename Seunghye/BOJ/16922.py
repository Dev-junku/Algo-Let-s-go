def backtrack(r_idx, num_left):
    global now_num

    # 모든 로마숫자 사용 완료
    if not num_left:
        numbers.append(now_num)
        return

    # I~L을 모두 사용했으나, 아직 여석이 남음
    if r_idx == 4:
        return

    # 남은 칸 중 일부를 채우고, 다음 순서에 넘기고, 복구
    for i in range(num_left+1):
        now_num += roman[r_idx] * i
        backtrack(r_idx + 1, num_left - i)
        now_num -= roman[r_idx] * i


N = int(input())
roman = [1, 5, 10, 50]
numbers = []
now_num = 0
backtrack(0, N)
print(len(set(numbers)))
