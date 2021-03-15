# import sys

# sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N, A, B = map(int, input().split())
    print('#{} {} {}'.format(t, min(A, B), max(A+B-N, 0)))