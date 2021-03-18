def solution(n, times):
    answer = 0
    max_time = max(times) * n
    start = 1
    end = max_time

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for time in times:
            cnt += (mid // time)

        if cnt < n:
            start = mid + 1
        elif cnt >= n:
            answer = mid
            end = mid - 1
    print(answer)
    return answer

solution(6, [7,10])