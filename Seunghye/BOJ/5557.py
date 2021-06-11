# 새로운 숫자를 더하거나, 빼거나.
# 이전 숫자까지 만들어진 등식의 결과 수를 저장
# 음수나 20 이상은 제외; 0~20까지만 저장
# 최종적으로 마지막 수와 같은 결과가 나오는 등식의 수를 반환

N = int(input())
numbers = list(map(int, input().split()))
results = [[0 for _ in range(21)] for _ in range(2)]
results[0][numbers[0]] = 1     # 첫 수는 무조건 더해짐
r_idx = 0

for i in range(1, N-1):
    r_idx = 1 - r_idx
    for j in range(21):
        # 빼서만 만들어질 수 있는 수
        if j < numbers[i]:
            results[r_idx][j] = results[1-r_idx][j+numbers[i]]
        # 더해서만 만들어질 수 있는 수
        elif j + numbers[i] > 20:
            results[r_idx][j] = results[1-r_idx][j-numbers[i]]
        # 빼기, 더하기 두 가지 식의 결과가 될 수 있는 수
        else:
            results[r_idx][j] = results[1-r_idx][j+numbers[i]] + results[1-r_idx][j-numbers[i]]

print(results[r_idx][numbers[N-1]])