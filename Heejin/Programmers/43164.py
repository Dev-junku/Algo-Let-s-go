# def solution(tickets):
#     answer = ['ICN']
#     result = list(filter(lambda x:x[0]=="ICN", tickets))
#     result.sort(key=lambda x:x[1])
#     queue = [result.pop(0)]
#
#     while queue:
#         current = queue.pop(0)
#         tickets.remove(current)
#         cur_end = current[1]
#         answer.append(cur_end)
#         tmp = []
#         for ticket in tickets:
#             if ticket[0] == cur_end:
#                 tmp.append(ticket)
#
#         if tmp:
#             tmp.sort(key=lambda x: x[1])
#             queue.append(tmp.pop(0))
#
#     return answer

# def dfs(current, tickets, answer):
#     if len(tickets) == 0:
#         answer.append(current[1])
#         return answer
#     else:
#         answer.append(current[1])
#         result = list(filter(lambda x:x[0] == current[1], tickets))
#         if len(result) > 1:
#             result.sort(key=lambda x:x[1])
#         current = result.pop(0)
#         tickets.remove(current)
#         return dfs(current, tickets, answer)
#
# def solution(tickets):
#     answer = ['ICN']
#     result = list(filter(lambda x:x[0]=="ICN", tickets))
#     result.sort(key=lambda x:x[1])
#     current = result.pop(0)
#     tickets.remove(current)
#     return dfs(current, tickets, answer)

def dfs(start, tickets, result):
    if len(tickets) == 0:
        return result
    for i, ticket in enumerate(tickets):
        if start == ticket[0]:
            end = ticket[1]
            tickets.pop(i)
            result.append(end)
            tmp = dfs(end, tickets, result)
            if len(tmp) != 0:
                return tmp
            result.pop()
            tickets.insert(i, [start, end])
    return []
def solution(tickets):
    tickets.sort()
    start = 'ICN'
    result = [start]
    answer = dfs(start, tickets, result)

    return answer

print(solution([['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]))
