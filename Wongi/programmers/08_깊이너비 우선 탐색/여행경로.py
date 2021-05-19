def solution(tickets):
    answer = []
    trips = {}
    for ticket in tickets:
        departure, destination = ticket
        trips[departure] = trips.get(departure, []) + [destination]

    # 정렬합니다.
    trips = {key : sorted(trips[key]) for key in trips.keys()}

    # dfs 재귀를 활용하여 여행경로를 구합니다.
    def dfs(v):
        while trips.get(v, 0):
            dfs(trips[v].pop(0))
        answer.append(v)
    
    # print(trips)
    dfs("ICN")
    return answer[::-1]
    
    