import sys
sys.stdin = open("sample_input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    # 인덱스: 출석 번호, 값: [지목한 사람들] 인 리스트 Tree
    tree = [[] for _ in range(N+1)]
    for i in range(len(info)//2):
        parent, child = info[i*2:(i+1)*2]
        tree[parent].append(child)
    # 그룹들을 담을 리스트
    groups = []
    for i in range(len(tree)):
        for j in range(len(tree[i])):
            for k in range(len(groups)):
                # 만약 현재 인덱스(출석번호) 가 이미 그룹들 중에 있거나, 현재 인덱스가 지목한 사람이 이미 그룹들 중에 있다면
                if i in groups[k] or tree[i][j] in groups[k]:
                    # 둘 다 그 그룹에 추가한다. set 이므로 중복은 자동 제거된다.
                    groups[k].add(i)
                    groups[k].add(tree[i][j])
                    break
            # for 문을 다 돌았는데 break 를 만나지 못했다면
            else:
                # 새로 그룹을 만들어서 추가한다.
                tmp = set()
                tmp.add(i)
                tmp.add(tree[i][j])
                groups.append(tmp)
    result = len(groups)

    # 그룹에 속하지 못한 사람의 숫자를 결과에 더한다.
    for i in range(1, N+1):
        for k in range(len(groups)):
            if i in groups[k]:
                break
        else:
            result += 1
    print("#{} {}".format(tc, result))
