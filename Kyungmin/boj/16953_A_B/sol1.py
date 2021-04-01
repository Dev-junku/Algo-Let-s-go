import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
result = 1

while a <= b:
    if b % 10 == 1:
        b = b // 10
        result += 1
        if a >= b:
            break
    elif not b % 2:
        b = b // 2
        result += 1
        if a >= b:
            break
    else:
        result = -1
        break
if a != b:
    result = -1
print(result)
