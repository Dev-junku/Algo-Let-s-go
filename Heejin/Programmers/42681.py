def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [1] + [0] * (n-1)

    while sum(visited) != n:
        for cost in costs:
            if visited[cost[0]] or visited[cost[1]]:
                if visited[cost[0]] and visited[cost[1]]:
                    continue
                else:
                    visited[cost[0]] = 1
                    visited[cost[1]] = 1
                    answer += cost[2]
                    break
    return answer

solution(4, [[2,3,8],[0,1,1],[0,2,2],[1,2,5],[1,3,1]])
