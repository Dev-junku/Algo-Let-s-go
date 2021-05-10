N = int(input())
towers = list(map(int, input().split()))
reciever = ['0' for _ in range(N)]

stack = []
for i in range(N-1, -1, -1):
    # 높은 탑을 만나면 바로 거기에서 수신됨
    while stack and stack[-1][1] <= towers[i]:
        j, _ = stack.pop()
        reciever[j] = str(i+1)
    # 낮은 탑이라면 해당 탑을 저장
    stack.append([i, towers[i]])

print(' '.join(reciever))
