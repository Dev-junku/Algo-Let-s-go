def solution(begin, target, words):
    visited = []
    count = 0
    queue = [begin]
    tmp = []
    while queue:
        current = queue.pop(0)
        visited.append(current)
        if current == target:
            return count
        else:
            for word in words:
                if word not in visited:
                    for i in range(len(word)):
                        if word[i] != current[i] and word[0:i] == current[0:i] and word[i + 1:] == current[i + 1:]:
                            tmp.append(word)
            if len(queue) == 0:
                queue += tmp
                count += 1
                tmp = []

    return 0

