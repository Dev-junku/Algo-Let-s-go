import sys
sys.stdin = open('input.txt')
from collections import deque
from queue import Queue

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
Time = 0
while trucks:
    cur = trucks[0]                            #현재트럭
    bridge.pop(0)                              #1초가 지나면 한칸 이동
    if cur + sum(bridge) <= L:                 #트럭 진입
        bridge.append(cur)
        trucks.pop(0)                          #진입한경우 브릿지 큐에 append 하고 남은 trucklist pop
    else:                                      #진입 못하는 경우 위에서 뺀 0때문에 0을 추가
        bridge.append(0)

    Time += 1

print(Time + w)

# concept > 트럭이 다 들어가는 거까지 시간 구하기 그래서 그 시간에 브릿지의 길이만큼 더해서 시간 구하기

#그대로 문제를 구현만 하면되는 문제 문제를 보자 마자 큐를 떠올렸고 그냥 그렇게 풀었다.
