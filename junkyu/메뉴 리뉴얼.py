from itertools import combinations
from collections import Counter

def solution(orders, course):
    res = []

    for c in course:
        res1 = []
        for order in orders:
            pair = combinations(sorted(order), c)
            res1 += pair
        
        cnt = Counter(res1)
        print(cnt)
        if len(cnt) != 0 and max(cnt.values()) != 1:
            res += [''.join(i) for i in cnt if cnt[i] == max(cnt.values())]
        
    return sorted(res)
           

if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
    print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))