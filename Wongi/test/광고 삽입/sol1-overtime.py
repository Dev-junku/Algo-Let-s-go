def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    total_logs = []
    
    play_h, play_m, play_s = map(int, play_time.split(':'))
    adv_h, adv_m, adv_s = map(int, adv_time.split(':'))
    
    def time_to_second(h, m, s):
        return s + (m * 60) + (h * 60 * 60)
    
    # second로 바꾸어 줍니다.
    total_play_second = time_to_second(play_h, play_m, play_s)
    total_adv_second = time_to_second(adv_h, adv_m, adv_s)
    # last_adv_time은 (전체 시간 - 광고 시간)이 됩니다.
    last_adv_time = total_play_second - total_adv_second
    
    # logs들도 (시작시간, runnig_time)으로 구해줍니다.
    for log in logs:
        log_start, log_end = log.split('-')
        log_start_h, log_start_m, log_start_s = map(int, log_start.split(':'))
        log_end_h, log_end_m, log_end_s = map(int, log_end.split(':'))
        
        total_log_start = time_to_second(log_start_h, log_start_m, log_start_s)
        total_log_end = time_to_second(log_end_h, log_end_m, log_end_s)
        total_log_ruuning = total_log_end - total_log_start
        total_logs.append((total_log_start, total_log_end, total_log_ruuning, log_start))
        
        
    total_logs.sort()
    # print(total_logs, total_play_second, total_adv_second, last_adv_time)
    
    # start 시작을 기점으로 total_adv_second의 최대 값을 찾습니다.
    max_second = 0
    for i in range(len(total_logs)):
        log = total_logs[i]
        log_start, log_end, log_running, l_start = log
        if log_start > last_adv_time: continue  # 마지막 광고 타임보다 크다면 패쓰...
            
        adv_start = log_start
        adv_end = adv_start + total_adv_second
        total_second = 0
        ans = 0
        for j in range(len(total_logs)):
            log2 = total_logs[j]
            log2_start, log2_end, log2_running, l_start = log2
            if log2_start > adv_end or log2_end < adv_start: continue
                
            if adv_start <= log2_start:
                adv_start = log2_start
            if adv_end >= log2_end:
                adv_end = log2_end
                
            total_second += adv_end - adv_start
            if max_second < total_second:
                max_second = total_second
                ans = log_start
                ans_index = i
                ans_start = l_start
        
        if ans:
            result = ans
            result_i = ans_index
            result_time = ans_start
    # print(result)
    # hours = result // 3600
    # minutes = (result - (3600 * hours)) // 60
    # # seconds = (result - (3600 * hours) - (60 * minutes))
    # print(hours, minutes, seconds, result_i)
    return str(total_logs[result_i][3])
    # print(result_time)