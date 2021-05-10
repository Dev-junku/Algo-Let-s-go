# 2. 순열 구하는 함수
def perm(idx, length):
    global word, cnt
    if idx == length:
        # 미리 구해놓은 긴 문자열에 있는 단어라면 cnt 더하기 
       if ''.join(word) in s_list:
           cnt += 1

    else:
        for change in range(idx, length):
            word[change], word[idx] = word[idx], word[change]
            perm(idx+1, length)
            word[idx], word[change] = word[change], word[idx]
        
            
# 0. 입력값을 받는다.
n, m = map(int, input().split())
word = list(input())
s = list(input())
arr = [i for i in range(n)]
cnt = 0
# 1. 구간을 나눠서 n의 길이만큼 빈 문자열에 저장해준다
s_list = []
for i in range(m-n+1):
    s_list.append(''.join(s[i:i+n]))
# 2. 순열 구하는 함수 실행
perm(0, n)
# 3. 개수 출력 
print(cnt)



# n, m = map(int, input().split())
# g = input()
# s = input()
# glit =[0]*52
# slit =[0]*52

# for i in range(n): #glit에 알파벳에 맞게 숫자 카운팅
#     if ord("a") <= ord(g[i]) and ord(g[i]) <= ord("z"):
#         glit[ord(g[i])-ord('a')] += 1
#     else:
#         glit[ord(g[i])-ord('A')+26] += 1

# for i in range(n):#s중에서 n개만큼만 선택
#     if ord("a") <= ord(s[i]) and ord(s[i]) <= ord("z"):
#         slit[ord(s[i])-ord('a')] += 1
#     else:
#         slit[ord(s[i])-ord('A')+26] += 1
# cnt = 0
# for i in range(m-n+1):
#     fail = False
#     for j in range(52):
#         if glit[j] != slit[j]:
#             fail = True
#             break
#     if fail == False:
#         cnt += 1
#     if i == m-n:
#         break

#     pos =0
#     if ord('a') <= ord(s[i]) and ord(s[i]) <= ord('z'):
#         pos = ord(s[i])-ord('a')
#     else:
#         pos = ord(s[i])-ord("A")+26
#     slit[pos] -= 1

#     if ord('a') <= ord(s[i+n]) and ord(s[i+n]) <= ord('z'):
#         pos = ord(s[i+n])-ord('a')
#     else:
#         pos = ord(s[i+n])-ord("A")+26
#     slit[pos] += 1

# print(cnt, end="")


