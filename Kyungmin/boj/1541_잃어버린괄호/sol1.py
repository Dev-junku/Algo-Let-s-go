import sys
sys.stdin = open('input.txt')

inp = input()
i = 0
lst = []
result = 0

# 인풋 처리
while i <= len(inp):
    if inp[i].isdigit():
        j = 0
        tmp = ''
        while inp[i+j].isdigit():
            tmp += inp[i+j]
            j += 1
            if i+j >= len(inp):
                break
        lst.append(int(tmp))
        i += len(tmp)
        if i >= len(inp):
            break
    else:
        lst.append(inp[i])
        i += 1

# 덧셈부터 먼저 다 해준다.
idx = 0
while '+' in lst:
    if lst[idx] == '+':
        tmp = 0
        p = lst.pop(idx-1)
        lst.pop(idx-1)
        q = lst.pop(idx-1)
        tmp += p + q
        idx -= 1
        lst.insert(idx, tmp)
        continue
    idx += 1
# 뺄셈
for i in range(len(lst)):
    if i == 0:
        result += lst[i]
    elif not i % 2:
        result -= lst[i]
print(result)
