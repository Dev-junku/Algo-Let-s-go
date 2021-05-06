# 초 변환 함수
def transSecond(time):
    total_second = int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])
    return total_second

# 풀이
def solution(play_time, adv_time, logs):

    if play_time == adv_time:
        return '00:00:00'

    logs.sort()
    answer = [0, 10987654321, "00:00:00"]
    ad_time = transSecond(adv_time)
    for pivot in logs:
        seco = 0
        ps = transSecond(pivot[0:8])
        pe = ps + ad_time
        for log in logs:
            log_s = transSecond(log[0:8])
            log_e = transSecond(log[9:17])
            
            if pe < log_s:
                continue

            if ps <= log_s and log_e <= pe:
                seco += log_e - log_s 
            elif ps <= log_s <= pe and pe <= log_e:
                seco += pe - log_s
            elif log_s < ps and  pe < log_e:
                seco += ad_time
            elif log_s <= ps <= log_e and log_e <= pe:
                seco += log_e - ps

        if answer[0] < seco:
            answer[0], answer[1], answer[2] = seco, ps, pivot[:8]
            
    return answer[2]

'''
22점 맞음 ㅎ
'''

if __name__ == '__main__':
    print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
    print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
    print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))