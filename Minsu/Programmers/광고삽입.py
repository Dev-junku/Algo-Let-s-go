# 시간을 초로 환산하는 함수
def tosecond(time):
    seconds = int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])
    return seconds


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

    total = [0] * (P+1)  # 전체 플레이 시간을 초로 나눈 리스트

    # 로그기록에서 시작시간에 1, 끝나는 시간에 -1 넣어주기
    for log in logs:
        start, end = map(str, log.split('-'))  # '-'기준으로 쪼개서 넣어주기
        start = tosecond(start)
        end = tosecond(end)

        total[start] += 1
        total[end] -= 1

    # 당시 시청하고 있는 시청자 수 구하기
    for i in range(1, P+1):
        total[i] = total[i-1] + total[i]

    # 초당 방송 누적 시청 수 구하기
    for i in range(1, P+1):
        total[i] = total[i-1] + total[i]

    # 최대 시간, 시작시간 초기화하기
    # 처음에 이부분을 간과했다가 엣지케이스가 생겼습니다.
    max_time = total[A-1]
    max_start = 0
    
    # 순회를 돌면서 최대시간 및 그때의 시작시간 구하기
    for i in range(P+1-A):
        if max_time < total[i+A] - total[i]:
            max_time = total[i+A] - total[i]
            max_start = i+1

    answer = tohour(max_start)
    return answer


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
