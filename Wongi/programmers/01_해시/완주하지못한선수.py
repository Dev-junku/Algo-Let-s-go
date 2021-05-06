def solution(participant, completion):
    # sol1
    # for comp in completion:
    #     participant.remove(comp)
    # return participant[0]

    # sol2
    result = {}
    for p in participant:
        result[p] = result.get(p, 0) + 1

    for c in completion:
        result[c] -= 1

    for key, value in result.items():
        if value > 0:
            return key