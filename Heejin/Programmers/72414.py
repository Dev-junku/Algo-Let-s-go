def timetosec(time):
    h, m, s = map(int, time.split(':'))
    m *= 60
    h *= 60 * 60
    return h + m + s

def solution(play_time, adv_time, logs):
    answer = ''
    times = []
    if play_time == adv_time:
        answer = '00:00:00'
    else:
        for idx, log in enumerate(logs):
            start, end = log.split('-')
            times.append((start, end))
        times.sort(key=lambda x:x[0])
        print(times)
        max_ectime = 0
        for i in range(len(times)):
            # 광고시간.
            start_play_time = timetosec(times[i][0])
            end_play_time = timetosec(times[i][1]) + timetosec(adv_time)
            ectime = 0

            for j in range(len(times)):
                start_time = timetosec(times[j][0])
                end_time = timetosec(times[j][1])
                if end_play_time < start_time:
                    break

                if start_play_time <= start_time:
                    ecstart = start_time
                else:
                    ecstart = start_play_time
                if end_play_time <= end_time:
                    ecend = end_time
                else:
                    ecend = end_play_time
                ectime += ecend - ecstart
            if ectime > max_ectime:
                max_ectime = ectime
                answer = times[i][0]

    return answer


solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])