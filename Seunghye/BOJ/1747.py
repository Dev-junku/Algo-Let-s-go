# 팰린드롬 확인
def is_palindrome(string):
    for i in range((len(string)+1)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

N = int(input())

# 소수 추출
sosu = [True for _ in range(1003002)]   # 1000000 이후 가장 작은 팰린드롬 소수
sosu[0] = False
sosu[1] = False
idx = 2
while idx < len(sosu):
    # N 이상의 소수일 경우, 팰린드롬 확인 후 출력
    if idx >= N and is_palindrome(str(idx)):
        print(idx)
        break
    # 해당되지 않을 경우, 배수 제거
    temp_idx = idx * 2
    while temp_idx < len(sosu):
        sosu[temp_idx] = False
        temp_idx += idx
    # 다음 소수 선택
    idx += 1
    while idx < len(sosu) and not sosu[idx]:
        idx += 1
