play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]


# 시간을 초로 환산하는 함수
def tosecond(time):
    h, m, s = map(int, time.split(':'))
    return (h * 3600 + m * 60 + s)


# 초에서 시간단위로 환산하는 함수
def tohour(time):
    h = time // 3600
    m = (time - (h*3600)) // 60
    s = time - (h*3600) - (m*60)
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    if s < 10:
        s = '0' + str(s)
    else:
        s = str(s)

    return (h + ':' + m + ':' + s)


def solution(play_time, adv_time, logs):
    P = tosecond(play_time)  # 전체 재생시간
    A = tosecond(adv_time)  # 광고 시간

    total = [0] * P # 전체 플레이 시간을 초로 나눈 리스트

    # 새로운 재생기록 리스트 만들기
    new_logs = []
    for log in logs:
        new_logs += (log.split('-'))  # '-'기준으로 쪼개서 넣어주기

    # 새로운 재생기록들을 초 단위로 바꿔주기
    for i in range(len(new_logs)):
        new_logs[i] = tosecond(new_logs[i])

    # 재생된 시간에 1씩 추가해주기
    for i in range(len(new_logs)//2):
        for j in range(new_logs[i*2], new_logs[i*2+1]):
            total[j] += 1

    results = []  # 결과들을 담는 리스트
    for start in range(P):
        end = (start + A if start + A <= P else P)  # 광고 끝 시간
        if sum(total[start:end]) not in results:
            results.append((sum(total[start:end])))
            if max(results) == sum(total[start:end]):
                max_idx = start

    answer = tohour(max_idx)
    return answer


print(solution(play_time, adv_time, logs))
