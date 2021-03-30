A, B = map(int, input().split())

count = 1       # 각 연산의 횟수
tovisit = [A]   # 연산 중간과정
found = False   # 찾았는지

while tovisit:
    # 연산 횟수단위 진행
    for _ in range(len(tovisit)):
        # 2를 곱한 수, 1을 오른쪽에 추가한 수 중 B보다 작은 수만 다음 연산 진행
        v = tovisit.pop(0)
        w = [2 * v, int(str(v) + '1')]
        for wi in w:
            # 찾았다면 순회 종료
            if wi == B:
                found = True
                break
            elif wi < B:
                tovisit.append(wi)
        if found:
            break
    else:
        count += 1

# 찾았다면 연산 최솟값+1, 찾지 못했다면(=만들 수 없다면) -1 출력
print(count + 1) if found else print(-1)
