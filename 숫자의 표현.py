def solution(n):
    
    cnt = 1
    i = 1
    while i < n//2 + 2:
        total = 0
        for j in range(i, n//2+2):
            total += j
            if total == n:
                cnt += 1
                break
            elif total > n:
                break
        i += 1
            
    return cnt


if __name__ == '__main__':
    print(solution(15))