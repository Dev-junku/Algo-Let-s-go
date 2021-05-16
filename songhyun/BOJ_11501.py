import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = 0
    cnt = 0
    acum = 0
    total = 0
    # print(numbers)
    for idx in range(len(numbers)-1, -1, -1):        #거꾸로 탐색
        if numbers[idx] >= max_num:
            max_num = numbers[idx]
            total += acum
            acum = 0
        if numbers[idx] < max_num:
            acum += max_num - numbers[idx]
        if idx == 0:
            total += acum
    print(total)

# concept : 예전에 swea에서 비슷한 문제 풀어본 듯 하다 뒤에서 부터 가장 큰거 잡고 빼가면 되는문제