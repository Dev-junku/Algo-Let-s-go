def solution(play_time, adv_time, logs):
    # 1. 문자열 입력값을 초로 변환
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)


    # 2. 구간별 배열
    all_time = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    # 3. 구간별 시청자 수 구하기
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    # 4. 구간별 시청자 수의 누적합 구하기
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    # 5. 플레이 타임동안 누적 시청자 수의 최대값인 구간 구하기 
    most_view = 0
    max_time = 0
    for start_time in range(1, play_time):
        if start_time + adv_time < play_time:
            end_time = start_time + adv_time
        else:
            end_time = play_time
        sum_played = all_time[end_time] - all_time[start_time]
        if most_view < sum_played:
            most_view = sum_played
            max_time = start_time + 1
    # 최대값 반환 
    return int_to_str(max_time)


# 1-1. 문자열을 숫자로 변환하는 함수
def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# 5-1. 숫자를 문자열로 변환하는 함수 
def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s