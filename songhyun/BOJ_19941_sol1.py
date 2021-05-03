import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
line = list(input())
visited = [False for _ in range(M)]
cnt = 0

for idx in range(len(line)): #라인만큼 순회
    if line[idx] == 'P':
        for j in range(idx-N, idx + N + 1):
            if j < 0 or j >= len(line):
                continue
            if visited[j] == False and line[j] == 'H':
                cnt += 1
                visited[j] = True
                break
print(cnt)


