# 최대공약수
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

s = input()
t = input()
a, b = len(s), len(t)


ss = s * (b // gcd(a, b))
tt = t * (a // gcd(a,b))


if ss == tt:
    result = 1
else:
    result = 0

print(result)