# 효율성 탈락
def solution(info, query):
    
    info_list = []
    for i in info:
        info_list.append(i.split())

    answer = []
    for q in query:
        c = q.split(' and ')
        c = c[:-1] + c[-1].split()
        num = 0
        for i in range(len(info_list)):
            cnt = 0
            for j in range(5):
                if c[j] == '-':
                    cnt += 1
                    continue
                else:
                    if c[j].isdigit():
                        if int(info_list[i][j]) >= int(c[j]):
                            cnt += 1
                    elif c[j] == info_list[i][j]:
                        cnt += 1

            if cnt == 5:
                num += 1

        answer.append(num)
    
    return answer